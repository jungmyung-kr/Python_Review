"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-04 04:28:37 ~ 04:38:43
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

'''
13. 원 그래프 (기본)
'''

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'ETC']

plt.pie(values, labels=labels, autopct='%.1f')
plt.pie(values, labels=labels, autopct='%.1f%%')  # %까지 출력 원한다면
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90)
# 90도 각도부터 데이터 나열되길 바란다면
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# 90도 각도이되, 시계 방향으로 나열되길 바란다면
plt.show()


values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'ETC']
explode = [0.2, 0.1, 0, 0, 0, 0]
# 0, 1번째 데이터만 따로 떼어서 보이게 하고 싶다면 거리 설정해주면 됨.
plt.pie(values, labels=labels, explode=explode)
plt.show()

# 전체 데이터가 균등한 거리로 떨어지게 하고 싶다면
explode = [0.05]*6
# 0, 1번째 데이터만 따로 떼어서 보이게 하고 싶다면 거리 설정해주면 됨.
plt.pie(values, labels=labels, explode=explode)
plt.show()

# 범례 표시
plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2, 0.3))
plt.show()

# 범례에 타이틀 표시
# plt.title('언어별 선호도')하면 차트 전체 위에 뜨지만, legend 안에 쓰면 범례 표 안에 뜸
plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2, 0.3), title='언어별 선호도')
plt.show()
