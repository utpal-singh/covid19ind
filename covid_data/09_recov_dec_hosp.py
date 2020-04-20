# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:44:39 2020

@author: utpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#convert dd-mm-yyyy to yyyy-mm-dd
df_stat = pd.read_csv('IndividualDetails.csv', parse_dates=['statuschangedate'], dayfirst = True)
recov = df_stat.loc[df_stat['currentstatus'] == 'Recovered']
decease = df_stat.loc[df_stat['currentstatus'] == 'Deceased']
hospitalised = df_stat.loc[df_stat['currentstatus'] == 'Hospitalized']


#newrecov = recov['statuschangedate']
#newrecov = pd.DataFrame(newrecov)
#newrecov.groupby([newrecov['statuschangedate'].dt.year, newrecov['statuschangedate'].dt.month, newrecov['statuschangedate'].dt.day]).count().plot(kind='bar')
#plt.tight_layout()
#plt.savefig('daily_recovery.jpg', dpi = 100)


#newdf = df['diagnosed_date']
#newdf = pd.DataFrame(newdf)
#newdf.groupby([newdf['diagnosed_date'].dt.year, newdf['diagnosed_date'].dt.month, newdf['diagnosed_date'].dt.day]).count().plot(kind='bar')
#plt.savefig('date_count_histo.jpg')

#newdecease = decease['statuschangedate']
#newdecease = pd.DataFrame(newdecease)
#newdecease.groupby(newdecease['statuschangedate'].dt.date).count().plot(kind='bar')
#plt.tight_layout()
#plt.savefig('daily_deceased.jpg', dpi = 100)

newhospit = hospitalised['statuschangedate']
newhospit = pd.DataFrame(newhospit)
newhospit.groupby(newhospit['statuschangedate'].dt.date).count().plot(kind='bar')
plt.tight_layout()
plt.savefig('daily_hospitalized.jpg', dpi = 100)