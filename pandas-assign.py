#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     19/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
print(df)

q=df.assign(varX = lambda x: x['A'] + x['B'],
                  varY = lambda x: x['A'] + x['C'])
print(q)
q.plot(kind='scatter', x='varX', y='varY')
plt.show()

q=(df.assign(varZ = lambda x: x['A'] + x['B'])
           .assign(varW = lambda x: x['B'] + x['D']))
q.plot(kind='scatter', x='varZ', y='varW')
plt.show()
print(q)


def main():
    pass

if __name__ == '__main__':
    main()
