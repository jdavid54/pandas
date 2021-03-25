import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

saturation = False
confinement = False

P = 60000000       # population
t = 100000         # taille de confinement
if confinement: P = t
N0 = 9043          # malades au début du confinement
E = 1              # personnes en contact par malade

#statistiques bing 
data1 = [9043,10995,12612,14459,16018,19856,22304,25233,29155,37575,40174]  # confirmés
data2 = [148, 372, 450, 562, 674, 860,1100,1331,1696,2314,2606]             # morts
data3 = [12,12,1300,1587, 2200, 2200, 3281,3900,4948,5700,7202]             # guéris
data4 = [a-(b+c) for a,b,c in zip(data1,data2,data3)]                       # actifs
print('Statistiques :')
print('- malades',data1)
print('- morts',data2)
print('- guéris',data3)
print('- actifs',data4)

#pour calculer le pic de contamination et le jour (quand data1 devient inférieur à mad_max)
mad_max = max(data1)               #max cas confirmés
index_max = data1.index(mad_max)   # index max dans data1

delta = [0]
[delta.append(a-b) for a,b in zip(data1[1:],data1[:-1])]
print('delta confimés', delta)

print(data1[1:])
print(data4[:-1])
taux_infection = [a/b for a,b in zip(delta[1:],data4[:-1])]      # delta confirmés(auj,hier) par rapport aux actifs d'hier
taux_décès = [a/b for a,b in zip(data2[1:],data1[:-1])]                   # par rapport aux malades confirmés d'hier
taux_guérison = [a/b for a,b in zip(data3[1:],data1[:-1])]                # par rapport aux malades confirmés d'hier
print(data4[-2],(40174-37575)/data4[-2])

# taux infection = delta(auj,hier)/actifs_hier      (40174-37575)/data4[-2]
# infection = confimés_hier*



print('\nEvolution taux infection:\n',taux_infection)
print('\nEvolution taux décès:\n',taux_décès)
print('\nEvolution taux guérison:\n',taux_guérison)


# taux de contamination pour évaluation de l'évolution
offset = -1
N = data4[offset]      # malades actifs aujourd'hui
print('\nEstimation à partir des chiffres du jour',offset)  # -1 : aujourd'hui
print('Nombre de malades hier :',N)

p = taux_infection[offset]    # taux d'infection
d = taux_décès[offset]        # taux de décès
g = taux_guérison[offset]     # taux de guérison
print('Taux :')
print('- infection :', '{:1.2f}%'.format(p*100))
print('- décès :', '{:1.2f}%'.format(d*100))
print('- guérison :', '{:1.2f}%'.format(g*100))

def nextday(N):    #delta confirmés du jour suivant
    global P, p, saturation
    if saturation : p = 0; return N
    return (N*E*p)

print('Nombres d\'actifs aujourd\'hui :',N)
nxtd = nextday(N)    # aujourd'hui
print('Delta contaminés demain :',nxtd)
print('Confirmés demain :', data1[-1]+nxtd)

p = 0
d = 0
g = 0.8
def evolution(ndays):
    global P,saturation, mad_max, index_max  
    n = data1            # cumul du nombre de malades
    m = data2            # morts par jour
    s = data3            # guérisons par jour
    a = data4            # actifs par jour
    #t = taux_infection
    c = delta            # évolution confirmés
    ppl = [P,]           # évolution population (décompte des morts)
    N = data1[-1]        # confirmés aujourd'hui
    pic = False
    lastN = data1[-1]    # repère confirmés hier pur calculer le pic
    decompte = data2[-1] + data3[-1]  # morts + guéris du jour
    for i in range(ndays):
        if N < 1 : break         # si plus de malades, fin de l'épidémie
        N = N - decompte              # actifs du jour
        N = nextday(N) + n[-1]        # cas confirmés le jour suivant
        if N > mad_max : mad_max = int(N)
        if N > P : N = P; mad_max = N; saturation = True   # quand toute la population est malade 
        m.append(int(N*d))            # évolution du nombre des morts, d:taux de décès parmi les malades
        P = P-N*d                     # décompte des morts de la population
        ppl.append(int(P))            # évolution de la population
        s.append(int(N*g))            # évolution du nombre des guéris, g:taux de guérison parmi les malades            
        n.append(int(N))              # évolution du nombre des malades        
        if N < lastN and not pic:
            print('Pic atteint le jour', index_max+i, 'avec',mad_max,'infectés'); pic = True
        c.append(int(N-lastN))        # évolution du nombre des cas confirmés par jour
        decompte = int(N*(d+g))       # decompte des morts et des guéris du nombre des malades
        a.append(int(N-decompte))     # évolution des actifs
        lastN = N                     # malades du jour pour calcul évolution du demain
        
    print('Dernier jour épidémie dans',i,'jours')
    #print(n,max(n)/P)
    #print(m,max(m)/P)
    print('Total de morts :',max(np.cumsum(m)))
    return i,ppl,n,m,s,c

# projection de la contamination à partir des taux du jour
i,p,n,m,s,c = evolution(100)

def draw(n,m,s,p):
    fig, ax = plt.subplots() 
    x = np.arange(len(n))
    y = n                    # évolutrion du nombre des malades
    z = np.cumsum(m)         # évolution du nombre des morts
    w = np.cumsum(s)         # évolution du nombre des guéris
    v = p                    # évolution de la population
    if max(n)>1e7 :
        #plt.plot(x,v, label='total population')
        ax.set_ylabel('dizaines de millions')    
    plt.plot(x,z, label='total morts')
    #plt.plot(x,w, label='total guéris')
    plt.plot(x,y, label='malades/jour')
    plt.plot(x,m, label='morts/jour')
    plt.plot(x,s, label='guéris/jour')
    ax.set_xlabel('Jours')                   
    
    plt.legend()
    plt.show()
    
draw(n,m,s,p)

def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:1.2f}%'.format(height*100),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x * 1e-6)

def percent(x, pos):
    'The two args are the value and tick position'
    return '%1.1f' % (x * 100)

from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(percent)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
x = np.arange(len(taux_infection))  
width = 0.2  # the width of the bars 
cols = ['% infection', '% décès','% guéris']
rects1 = ax.bar(x - width, taux_infection, width, label=cols[0])
rects2 = ax.bar(x , taux_décès, width, label=cols[1])
rects3 = ax.bar(x + width, taux_guérison, width, label=cols[2])
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Taux')
ax.set_xlabel('Dates de confinement')
ax.set_title('Evolution Infection, Décès, Guérison')
ax.set_xticks(x)
labels = ('20/03','21/03','22/03','23/03','24/03','25/03','26/03','27/03','28/03','29/03')
ax.set_xticklabels(labels)
autolabel(ax, rects1)
autolabel(ax, rects2)
autolabel(ax, rects3)
fig.tight_layout()
ax.legend()
fig.tight_layout()
plt.show()

# evolution malades et morts
fig, ax1 = plt.subplots()
color = 'tab:blue'
x = np.arange(len(c))
y = n                  #[k*(k>=0) for k in np.cumsum(c)]
z = np.cumsum(m)
ax1.plot(x,y, label='progression malades', color=color)
ax1.set_ylabel('malades', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xlabel('Jours')
#ax1.legend()
color = 'tab:red'
ax2 = ax1.twinx()
ax2.plot(x,z, label='total morts', color=color)
ax2.set_ylabel('morts', color=color)
ax2.tick_params(axis='y', labelcolor=color)
if max(z)>1e7 : ax2.set_ylabel('dizaines de millions')
fig.tight_layout()
#ax2.legend()
plt.show()

