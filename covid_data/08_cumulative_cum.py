# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:21:49 2020

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

sns.barplot(x = 'date', y = 'totalconfirmed', data = df)
plt.tight_layout()
#a1.figure.savefig('conf_cum_plot.jpg', dpi = 100)
plt.savefig('conf_cum_plot.jpg', dpi = 100)