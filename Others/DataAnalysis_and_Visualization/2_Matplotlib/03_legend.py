"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-29 03:11:25 ~ 03:15:55
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

'''
3. 범례
'''

plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='upper right')
'''
Location String : Location Code
best : 0
upper right : 1
upper left : 2
lower left : 3
lower right : 4
right : 5
center left : 6
center right : 7
lower center : 8
upper center : 9
center : 10
'''

plt.plot(x, y, label='범례')
plt.legend(loc=(0.7, 0.8))  # x축, y축 (0~1 사이)
