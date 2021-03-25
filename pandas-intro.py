#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# link : http://ghajba.developpez.com/tutoriels/python/analyse-donnees-avec-pandas/#LI
# Author:      Jean
#
# Created:     18/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np

#objet de type series qui contient plusieurs valeurs différentes
series = pd.Series([1,2,3,4,5, np.nan, "a string", 6])
print(series)
series = pd.Series([1,2,np.nan, 4])
print(series)
#DataFrames est un tableau à deux dimensions
df = pd.DataFrame(np.array([1,2,3,4,5,6]).reshape(2,3))
print(df)

#Le paramétrage par défaut affiche l'indice numérique des lignes et des colonnes,
#mais il peut être modifié pour donner plus de sens aux données
df = pd.DataFrame(np.array([1,2,3,4,5,6]).reshape(2,3), columns=list('ABC'), index=list('XY'))
print(df)

#méthode head() affiche les n premières lignes fournies comme argument.
#Si vous ne fournissez pas d'argument, la valeur par défaut sera 5
df2 = pd.DataFrame(np.arange(1, 7501).reshape(500,15))
print(df2.head(2))
print(df2.head())
#méthode tail() affiche les n dernières lignes du DataFrame. Par défaut, 5
print(df2.tail())
print(df2.tail(1))
#La fonction describe() est la fonctionnalité que nous allons
#fréquemment utiliser pour analyser un nouvel ensemble de données
data=np.arange(1, 100, 0.12)
#print('data=',np.arange(1, 100, 0.12))     data.size = 825 = 33*25
df3 = pd.DataFrame(data.reshape(33,25))
print(df3.describe())
#Pour sectionner une partie d'un Dataframe, il faut utiliser l'attribut iloc[]
print(df3.iloc[:5,:10])
print(df3.iloc[-5:])      # df3.tail(5)
print(df3.iloc[:5])       # df3.head(5)
#rename
df4 = df3.rename(columns=lambda c: chr(65+c))
print(df4.loc[:5, 'A':'D'])

baby_names = pd.read_csv('baby_names.csv')
print(baby_names.head())
print(baby_names.describe())
print(baby_names.head())
print(baby_names.sort_values(by='Count').head())
print(baby_names.sort_values(by='Count', ascending=False).head())



def main():
    pass

if __name__ == '__main__':
    main()
