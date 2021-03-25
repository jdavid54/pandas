import pandas as pd

def load(filename):
    temp = '%s.csv'
    path = temp % filename
    print(path)
    return pd.read_csv(path)

data = load('csv/titanic')
print (data, data.columns)

bysex = data['sex'].value_counts()
print(bysex)

byage = data['age'].value_counts()
print(byage)

result = data.groupby(['sex','age'])['sex'].count()
print(result)

result = data.groupby(['class','sex'])['sex'].count()
print(result)

result = data.groupby(['sex','age','survived'])['survived'].count()
print(result)

result = data.groupby(['age','sex','survived'])['survived'].count()
print(result)