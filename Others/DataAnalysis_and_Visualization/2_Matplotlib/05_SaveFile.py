"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-31 03:35:48 ~ 03:39:50
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)
plt.savefig('graph.png')

# 그래프 사이즈 지정 저장
plt.savefig('graph.png', dpi=100)


plt.figure(dpi=200)  # 화면에 보여지는 사이즈
plt.plot(x, y)
plt.savefig('graph_200.png', dpi=100)  # 저장되는 사이즈