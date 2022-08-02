"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-02 03:44:17 ~ 03:49:50
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

'''
COVID-10 백신 종류별 접종 인구
'''
days = [1, 2, 3]  # day 1, day 2, day 3
az = [2, 4, 8]  # (단위 : 만명) 1일부터 3일까지 아스트라제네카 접종인구
pfizer = [5, 1, 3]  # 화이자
moderna = [1, 2, 5]  # 모더나

plt.plot(days, az)
plt.plot(days, pfizer)
plt.plot(days, moderna)

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', linestyle='-.')
plt.legend(ncol=3)  # 그래프 내 공간이 좁을 경우 범례에 사용할 수 있는 방법