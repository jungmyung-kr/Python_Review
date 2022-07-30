"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-29 03:05:23 ~ 03:11:24
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

'''
2. 축
'''

# title

plt.plot(x, y)
plt.title('꺾은선 그래프', fontdict={'family': 'Maplestory OTF', 'size': 20})
# 기본 폰트는 애플고딕이지만, 개별적으로 설정도 가능

# label

plt.plot(x, y)
plt.xlabel('X축', color='red', loc='right')
# x축 loc : left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top')
# y축 loc : top, center, bottom

# tick

plt.plot(x, y)
plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()