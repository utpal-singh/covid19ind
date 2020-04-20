# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:24:06 2020

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

sns.barplot(x = 'date', y = 'totalrecovered', data = df)
plt.tight_layout()
#a3.figure.savefig('recovered_cum_plot.jpg', dpi = 100)
plt.savefig('recovered_cum_plot.jpg', dpi = 100)