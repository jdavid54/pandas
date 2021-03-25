#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     08/03/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd

titanic3_df=pd.read_excel('titanic3.xls', index_col=0)
print(titanic3_df.head)
