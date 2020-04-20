# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:06:58 2020

@author: utpal
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:28:33 2020

@author: utpal
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 08:26:16 2020

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

class Plots():

      def a1(self):
            sns.barplot(x = 'date', y = 'totalconfirmed', data = df)
            plt.tight_layout()
            #a1.figure.savefig('conf_cum_plot.jpg', dpi = 100)
            plt.savefig('conf_cum_plot.jpg', dpi = 100)
            
      def a2(self):
      
            sns.barplot(x = 'date', y = 'totaldeceased', data = df)
            plt.tight_layout()
      #      a2.figure.savefig('decease_cum_plot.jpg', dpi = 100)
            plt.savefig('decease_cum_plot.jpg', dpi = 100)
            
      def a3(self):
      
            sns.barplot(x = 'date', y = 'totalrecovered', data = df)
            plt.tight_layout()
      #      a3.figure.savefig('recovered_cum_plot.jpg', dpi = 100)
            plt.savefig('recovered_cum_plot.jpg', dpi = 100)
            
      #def a4():
      #
      #      plt.plot(date, dailyconfirmed)
      #      plt.tight_layout()
      #      plt.savefig('conf_daily_plot.jpg', dpi = 100)
            
      def a4(self):
      
            sns.barplot(x = 'date', y = 'dailydeceased', data = df)
            plt.tight_layout()
      #      a4.figure.savefig('decease_daily_plot.jpg', dpi = 100)
            plt.savefig('decease_daily_plot.jpg', dpi = 100)
      
      def a5(self):
            sns.barplot(x = 'date', y = 'dailyrecovered', data = df)
            plt.tight_layout()
      #      a5.figure.savefig('recover_daily_plot.jpg', dpi = 100)
            plt.savefig('recover_daily_plot.jpg', dpi = 100)
      
      def a6(self):
            corr = df.corr()
            sns.heatmap(corr)
            plt.tight_layout()
      #      a6.figure.savefig('heat_map.jpg', dpi = 100)
            plt.savefig('heat_map.jpg', dpi = 100)
            
      def a7(self):
            
            sns.pairplot(df)
            plt.tight_layout()
      #      a7.savefig('pair_plot.jpg', dpi = 100)
            plt.savefig('pair_plot.jpg', dpi = 100)
      
      def a8(self):
            sns.distplot(mar15['dailyconfirmed'], bins = 25)
            plt.tight_layout()
            #fig8 =  a8.get_figure()
            #fig8.savefig('dailyconf_dist_15mar.jpg', dpi = 100)
            plt.savefig('dailyconf_dist_15mar.jpg', dpi = 100)
      
plot = Plots()

plot.a1()
plot.a2()
plot.a3()
plot.a4()