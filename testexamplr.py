# create a list of list with the employee details using that list create pandas dataframe


import pandas as pd

Employeedata=[['ZXY','1','Dev'],['ABC','2','Admin']
              ,['DEF','3','IT'],['JHI','4','QA']
              ]
# print("Employeedata" , Employeedata)
# datastoredinpandas=pd.DataFrame(Employeedata)
# print("datastoredinpandas -> ", datastoredinpandas)
# datastoredinpandas


import os


aa=(1,2,3)
try:
    aa[1]=5
except Exception as E:
    print(E)

# filepath=r'emptyfile.txt'
# fileexist=os.path.exists(filepath)
# try:
#     print(fileexist)
# except Exception as EK:
#     print(EK , "")


# import camelot

# aa=camelot.read_pdf(r'Input/Invoice_425561.pdf')
# print(aa)

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
print(housing.data.shape, housing.target.shape)
print(housing.feature_names[0:6])