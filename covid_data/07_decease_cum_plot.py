# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:22:53 2020

@author: utpal
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('national.csv')

mar15 = df[47:]

date = df['date']
totalconfirmed = df['totalconfirmed']
totaldeceased = df['totaldeceased']
totalrecovered = df['totalrecovered']
dailyconfirmed = df['dailyconfirmed']
dailydeceased = df['dailydeceased']
dailyrecovered = df['dailyrecovered']

sns.barplot(x = 'date', y = 'totaldeceased', data = df)
plt.tight_layout()
#a2.figure.savefig('decease_cum_plot.jpg', dpi = 100)
plt.savefig('decease_cum_plot.jpg', dpi = 100)