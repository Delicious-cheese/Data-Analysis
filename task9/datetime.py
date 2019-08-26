# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from datetime import datetime


print(np.random.randn(6))
ts = pd.Series(np.random.randn(6))
# 没有设定index的时候, 自动从0开始
#print(ts)

print()

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
print()

print('步长为1')
print(ts[::])
print('步长为2')
print(ts[::2])

print()
print(ts + ts[::2])

# 索引与其他的一样,直接取index这里可以用有意义的字符串表示日期
print()
print(ts['1/10/2011'])
print(ts['20110110'])

# 手动写date的index很麻烦， 可以用pd.date_range('1/1/2011')
long_ts = pd.Series(np.random.randn(20), index=pd.date_range('1/1/2010', periods=20))
print(long_ts)

print()
print(ts[datetime(2011, 1, 7):])
# 取值的时候可以字符串，datetime这样的函数用逗号隔开
# print(ts[datetime('20110107')])

print()
print(ts['1/6/2011': '1/11/2011'])
print('两种情况是否都行')
# 月放在前面
print(ts['20110106': '2011/01/11'])

print()
print('变化前')
print(ts)
print('变化后')
print(ts.truncate(after='1/7/2011'))

print()
dates = pd.date_range('1/1/2000', periods=1000) #?freq
long_df = pd.DataFrame(np.random.randn(1000, 4), index=dates, columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(long_df)
print()
print(long_df.loc['5-2001'])