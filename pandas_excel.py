#-------------------------------------------------------------------------------
# Name:        pandas reading excel file
# Purpose:
#
# Author:      Jean
#
# Created:     08/03/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd

print(pd.ExcelFile('titanic3.xls'))
titanic3_df=pd.read_excel('titanic3.xls', index_col=0)
print(titanic3_df.head)