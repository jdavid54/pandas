#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     18/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
from IPython.core.display import Image
Image('http://akamaicovers.oreilly.com/images/0636920023784/lrg.jpg')

import quandl as q
q.ApiConfig.api_key='4U3pyyWnY5DUacmTLH11'
aapl_table = q.get('EOD/AAPL')     #https://www.quandl.com/search?query=aapl end of day apple
print(aapl_table)
"""
import pandas as pd
import numpy as np

temp = '%s.csv'
path = temp % 'EOD-AAPL'
print(path)
aapl_bars = pd.read_csv(path)
print (aapl_bars)


def main():
    pass

if __name__ == '__main__':
    main()
