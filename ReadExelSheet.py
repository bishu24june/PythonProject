'''
Created on Mar 14, 2020

@author: Bishwa
'''


import pandas as pd
#import xlrd as xl   #'''(Panda to be worked )'''
file = pd.ExcelFile("C:\Personal\Employee.xlsx")
print("File = ", file.sheet_names)
sheet = file.parse("Emp")
print("Sheet = \n", sheet)
print("Column = ",sheet.Name)
print("Column Sum = ",sheet.Salary.sum())
print("Location = \n",sheet.loc[0])