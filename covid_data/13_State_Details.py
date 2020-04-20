# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:11:46 2020

@author: utpal
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('IndividualDetails.csv')

rows_count = df.patientnumber.count()

class Statecoun():
    def AndhraPradesh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Andhra Pradesh':
                k = k+1
        return k
    
    def ArunachalPradesh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Arunachal Pradesh':
                k = k+1
        return k
    
    def Assam(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Assam':
                k = k+1
        return k
    
    def Bihar(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Bihar':
                k = k+1
        return k
    
    def Chhatisgarh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Chhattisgarh':
                k = k+1
        return k
    
    def Goa(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Goa':
                k = k+1
        return k
    
    def Gujarat(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Gujarat':
                k = k+1
        return k
    
    def Haryana(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Haryana':
                k = k+1
        return k
    
    def HimachalPradesh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Himachal Pradesh':
                k = k+1
        return k
    
    def Karnataka(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Kerala':
                k = k+1
        return k
    
    def Punjab(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Kerala':
                k = k+1
        return k
    
    def Jharkhand(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Jharkhand':
                k = k+1
        return k
    
    def Kerala(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Kerala':
                k = k+1
        return k
    
    def MadhyaPradesh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Madhya Pradesh':
                k = k+1
        return k
    
    def Maharashtra(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Maharashtra':
                k = k+1
        return k
    
    def Manipur(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Manipur':
                k = k+1
        return k
    
    def Meghalaya(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Meghalaya':
                k = k+1
        return k
    
    def Kerala(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Kerala':
                k = k+1
        return k
    
    def Mizoram(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Mizoram':
                k = k+1
        return k
    
    def Nagaland(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Nagaland':
                k = k+1
        return k
    
    def Odisha(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Odisha':
                k = k+1
        return k
    
    def Rajasthan(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Rajasthan':
                k = k+1
        return k
    
    def Sikkim(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Sikkim':
                k = k+1
        return k
    
    def TamilNadu(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Tamil Nadu':
                k = k+1
        return k
    
    def Telangana(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Telangana':
                k = k+1
        return k
    
    def Tripura(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Tripura':
                k = k+1
        return k
    
    def UttarPradesh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Uttar Pradesh':
                k = k+1
        return k
    
    def Uttarakhand(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Uttarakhand':
                k = k+1
        return k
    
    def WestBengal(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'West Bengal':
                k = k+1
        return k
    
    def AndamanNicobar(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Andaman and Nicobar Islands':
                k = k+1
        return k
    
    def Chandigarh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Chandigarh':
                k = k+1
        return k
    
    def Delhi(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Delhi':
                k = k+1
        return k
    
    def JammuKashmir(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Jammu and Kashmir':
                k = k+1
        return k
    
    def Ladakh(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Ladakh':
                k = k+1
        return k
    
    def Puducherry(self):
        k = 0
        for i in range(rows_count):
            if df.iloc[i][7] == 'Puducherry':
                k = k+1
        return k
  

Statecount = Statecoun()      

   
AndhraPradesh = Statecount.AndhraPradesh()
ArunachalPradesh = Statecount.ArunachalPradesh()
Assam = Statecount.Assam()
Bihar = Statecount.Bihar()
Chhatisgarh = Statecount.Chhatisgarh()
Goa = Statecount.Goa()
Gujarat = Statecount.Gujarat()
Haryana = Statecount.Haryana()
HimachalPradesh = Statecount.HimachalPradesh()
Jharkhand = Statecount.Jharkhand()
Karnataka = Statecount.Karnataka()
Kerala = Statecount.Kerala()
MadhyaPradesh = Statecount.MadhyaPradesh()
Maharashtra = Statecount.Maharashtra()
Manipur = Statecount.Manipur()
Meghalaya = Statecount.Meghalaya()
Mizoram = Statecount.Mizoram()
Nagaland = Statecount.Nagaland()
Odisha = Statecount.Odisha()
Punjab = Statecount.Punjab()
Rajasthan = Statecount.Rajasthan()
Sikkim = Statecount.Sikkim()
Telangana = Statecount.Telangana()
TamilNadu = Statecount.TamilNadu()
Tripura = Statecount.Tripura()
UttarPradesh = Statecount.UttarPradesh()
WestBengal = Statecount.WestBengal()
AndamanNicobar = Statecount.AndamanNicobar()
Chandigarh = Statecount.Chandigarh()
Delhi = Statecount.Delhi()
JammuKashmir = Statecount.JammuKashmir()
Ladakh = Statecount.Ladakh()
Puducherry = Statecount.Puducherry()



States = ['AndhraPradesh', 'ArunachalPradesh', 'Assam', 'Bihar', 'Chhatisgarh', 'Goa', 'Gujarat', 'Haryana', 'HimachalPradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'MadhyaPradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'TamilNadu', 'Telangana', 'Tripura', 'UttarPradesh', 'WestBengal', 'AndamanNicobar', 'Chandigarh', 'Delhi', 'JammuKashmir', 'Ladakh', 'Puducherry']
StateCoount = [AndhraPradesh, ArunachalPradesh, Assam, Bihar, Chhatisgarh, Goa, Gujarat, Haryana, HimachalPradesh, Jharkhand, Karnataka, Kerala, MadhyaPradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, TamilNadu, Telangana, Tripura, UttarPradesh, WestBengal, AndamanNicobar, Chandigarh, Delhi, JammuKashmir, Ladakh, Puducherry ]
#Sortcount = []
#
#for i in range(len(StateCoount)):
#      if StateCoount[i]<StateCoount[i-1]:
#            Sortcount.append(StateCoount[i])
#                  
#print(Sortcount)
            


plt.figure(figsize=(7,7))
statesplot = sns.barplot(StateCoount, States)
plt.tight_layout()
statesplot.figure.savefig('StatesConfirmed.jpg', dpi = 100, annot = True)