# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:49:16 2024

@author: ptmab
"""
import pandas as pd
file = pd.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())

file2 = pd.read_csv("diab_data.csv")
print(file2)
print(file2.info())
print(file2.describe())

file3 = pd.read_csv("housing_data.csv")
print(file3)
print(file3.info())
print(file3.describe())

file4 = pd.read_csv("iris.csv")
print(file4)
print(file4.info())
print(file4.describe())

#file5 = pd.read_txt("insurance_data.txt")
#print(file5)
#one cannot read text files with panda

#file5 = pd.read_csv("insurance_data.txt",sep=";")
#print(file5)

import pandas as taf
file = taf.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())

