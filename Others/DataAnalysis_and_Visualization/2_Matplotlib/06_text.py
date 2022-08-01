"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-01 03:39:51 ~ 03:44:16
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

plt.plot(x, y, marker='o')

for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.3, txt, ha='center', color='blue')

# 그래프에 좌표값도 같이 볼 수 있도록 설정하는 부분
