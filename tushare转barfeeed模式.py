# -*- coding: utf-8 -*-
"""

Created on Tue Jan 29 11:27:19 2019

@author: Administrator
"""
import tushare as ts  
import pandas as pd  
  
# 得到15分钟数据（股票002665,始于2018-01-01,止于2018-05-24,15分钟数据）  
data = ts.get_hist_data('002665','2017-01-01','2019-01-29')  
print(data)
# 数据存盘  
data.to_csv('F:/shuju/002665barf.csv',sep="," )  
# 读出数据，DataFrame格式  
df = pd.read_csv('F:/shuju/002665barf.csv')  
# 从df中选取数据段，改变段名；新段'Adj Close'使用原有段'close'的数据  
df2 = pd.DataFrame({'Date' : df['date'], 'Open' : df['open'],  
                    'High' : df['high'],'Low' : df['low'],  
                    'Close' : df['close'],'Volume' : df['volume'],  
                    })  
df2.sort_values(by="Date",inplace=True)
print(df2)
# 按照Yahoo格式的要求，调整df2各段的顺序  
dt = df2.pop('Date')  
df2.insert(0,'Date',dt)  
o = df2.pop('Open')  
df2.insert(1,'Open',o)  
h = df2.pop('High')  
df2.insert(2,'High',h)  
l = df2.pop('Low')  
df2.insert(3,'Low',l)  
c = df2.pop('Close')  
df2.insert(4,'Close',c)  
v = df2.pop('Volume')  
df2.insert(5,'Volume',v)  
# 新格式数据存盘，不保存索引编号  
df2["时间"]="16:00:00"
print(df2)
df2["Date Time"]=df2["Date"]+" "+df2["时间"]
df3=df2[["Date Time","Open","High","Low","Close","Volume"]]
print(df3)

df3.to_csv("F:/shuju/002665-barfeed.csv", index=False)