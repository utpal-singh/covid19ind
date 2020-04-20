# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:36:00 2020

@author: utpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IndividualDetails.csv', parse_dates=['dateannounced'], dayfirst = True)

newdf = df['dateannounced']
newdf = pd.DataFrame(newdf)

newdf.groupby(newdf['dateannounced'].dt.month).count().plot(kind='bar')
plt.tight_layout()
plt.savefig('monthly_confirm.jpg', dpi =100)

newdf.groupby([newdf['dateannounced'].dt.year, newdf['dateannounced'].dt.month, newdf['dateannounced'].dt.day]).count().plot(kind='bar')
plt.tight_layout()
plt.savefig('daily_confirm.jpg', dpi = 100)

fig = newdf.groupby(newdf['dateannounced'].dt.date).count().plot(kind='bar')

