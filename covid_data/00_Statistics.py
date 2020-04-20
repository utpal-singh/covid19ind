# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:04:00 2020

@author: utpal
"""

df = pd.read_csv('national.csv')
row_count = df.date.count()

confirmed = df.iloc[row_count -1][4]
dailyconfirmed = df.iloc[row_count -1][0]
deceased = df.iloc[row_count -1][5]
dailydeceased = df.iloc[row_count -1][1]
recovered = df.iloc[row_count -1][6]
dailyrecovered = df.iloc[row_count -1][2]
active = confirmed - deceased - recovered
activedailyinc = dailyconfirmed - dailydeceased - dailyrecovered

print('Confirmed: ', confirmed)
print('Day Increment Confirmed: ', dailyconfirmed)
print('Active: ', active)
print('Day Increment Active: ', activedailyinc)
print('Recovered', recovered)
print('Daily Increment Recovered: ', dailyrecovered)
print('Deaths: ', deceased)
print('Day Increment Deaths: ', dailydeceased)