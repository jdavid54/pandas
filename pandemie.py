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
data1 = [9043,10995,12612,14459,16018,19856,22304,25233]
data2 = [148, 372, 450, 562, 674, 860,1100,1331]
data3 = [12,12,1300,1587, 2200, 2200, 3281,3900]


taux_infection = [(a-b)/b for a,b in zip(data1[1:],data1[:-1])]
taux_décès = [a/b for a,b in zip(data2,data1)]
taux_guérison = [a/b for a,b in zip(data3,data1)]

print('Statistiques :')
print('- malades',data1)
print('- morts',data2)
print('- guéris',data3)
print('\nEvolution taux infection',taux_infection)
# taux
offset = -1
N = data1[offset-1]      # malades hier
print('\nEstimation à partir des chiffres du jour',offset)  # -1 : aujourd'hui
print('Nombre de malades jour d\'avant :',N)

p = taux_infection[offset]    # taux d'infection
d = taux_décès[offset]        # taux de décès
g = taux_guérison[offset]     # taux de guérison
print('Taux :')
print('- infection :', '{:1.2f}%'.format(p*100))
print('- décès :', '{:1.2f}%'.format(d*100))
print('- guérison :', '{:1.2f}%'.format(g*100))

def nextday(N):
    global P, p, saturation
    if saturation : p = 0; return N
    return int(N*(1+E*p))
print('Nombres de malades :')
print('- hier :',N)
nxtd = nextday(N)    # aujourd'hui
print('- aujourdhui :',nxtd)
demain = nextday(nxtd)     # le lendemain
print('- demain :',demain)

def evolution(ndays):
    global N,P,saturation  #,E,p,d,g
    n =[N,]    # nombre de malades
    m = [0,]   # morts par jour
    s = [0,]   # guérisons par jour
    c = [0,]   # cas de contamination par jour
    pol = [P,] # évolution population
    lastN = N  # malades du jour
    decompte = 0  # morts + guéris
    for i in range(ndays):
        if N < 1 : break            # si plus de malades, fin de l'épidémie
        #ni = P*(1 - N/P)        #population non infectée
        m.append(int(N*d))       # évolution du nombre des morts, d:taux de décès parmi les malades
        P = P - N*(d)            # décompte des morts de la population
        pol.append(int(P))       # évolution de la population
        s.append(int(N*g))       # évolution du nombre des guéris, g:taux de guérison parmi les malades
        actif = N-decompte       # malades pouvant contaminer
        N = nextday(actif)       # malades jour suivant 
        decompte = N*(d+g)       # decompte des morts et des guéris du nombre des malades
        if N > P : N = P; saturation = True   # quand toute la population est malade     
        n.append(int(N))         # évolution du nombre des malades        
        c.append(int(N-lastN))   # évolution du nombre des contaminés par jour
        lastN = N                # malades du jour pour calcul évolution du demain
    print('Dernier jour épidémie dans',i,'jours')
    #print(n,max(n)/P)
    #print(m,max(m)/P)
    print('Total de morts :',max(np.cumsum(m)))
    return i,pol,n,m,s,c

i,pol,n,m,s,c = evolution(1000)
cm = np.cumsum(m)    #cumul des morts sur la période

def draw(n,m,s,pol):
    fig, ax = plt.subplots() 
    x = np.arange(len(n))
    y = n                    # évolutrion du nombre des malades
    z = np.cumsum(m)         # évolution du nombre des morts
    w = s                    # évolution du nombre des guéris
    v = pol                  # évolution de la population
    plt.plot(x,v, label='total population')
    plt.plot(x,y, label='malades/jour')
    plt.plot(x,z, label='total morts')
    plt.plot(x,m, label='morts/jour')
    plt.plot(x,w, label='guéris/jour')
    ax.set_xlabel('Jours')                   
    ax.set_ylabel('dizaines de millions')
    plt.legend()
    plt.show()
    
draw(n,m,s,pol)

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
rects2 = ax.bar(x , taux_décès[1:], width, label=cols[1])
rects3 = ax.bar(x + width, taux_guérison[1:], width, label=cols[2])
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Taux')
ax.set_xlabel('Dates de confinement')
ax.set_title('Evolution Infection, Décès, Guérison')
ax.set_xticks(x)
labels = ('20/03','21/03','22/03','23/03','24/03','25/03','26/03')
ax.set_xticklabels(labels)
autolabel(ax, rects1)
autolabel(ax, rects2)
autolabel(ax, rects3)
#fig.tight_layout()
ax.legend()
fig.tight_layout()
plt.show()

# evolution malades et morts
fig, ax1 = plt.subplots()
color = 'tab:blue'
x = np.arange(len(c))
y = [k*(k>=0) for k in np.cumsum(c)]
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

