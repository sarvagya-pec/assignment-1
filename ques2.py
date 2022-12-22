# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:01:48 2022

@author: LENOVO
"""

a = int(input("Enter Gross income : "))
b = int(input("Number of dependents : "))

Tax_rate = 20
Standard_deduction = 10000
Dependent_deduction = 3000

Taxable_income = a-10000-(Dependent_deduction*b)
d = Taxable_income * Tax_rate
if Taxable_income < 0 :
    print("Tax = 0. No tax")
else:
    print(Taxable_income , " is taxable income.", d,"is the tax.")
