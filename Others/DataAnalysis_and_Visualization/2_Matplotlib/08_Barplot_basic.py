"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-02 03:49:51 ~ 03:58:09
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

'''
막대 그래프 (기본)
'''

labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키

plt.bar(labels, values)

# 색상 1
labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키

plt.bar(labels, values, color='r')

# 색상 2
labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키
colors = ['r', 'g', 'b']

plt.bar(labels, values, color=colors)
plt.bar(labels, values, color=colors, alpha=0.5)

# y축 범위 조절
labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키

plt.bar(labels, values)
plt.ylim(175, 195)  # y축 범위를 지정해줌으로써 데이터간 차이를 보다 잘 드러나게 함

# x축 바 두께 조절
plt.bar(labels, values, width=0.5)

# 텍스트 기울여 겹침 방지
plt.bar(labels, values, width=0.3)
plt.xticks(rotation=45)  # x축의 이름 데이터 각도를 45도로 설정
plt.yticks(rotation=45)  # y축의 이름 데이터 각도를 45도로 설정

# labels이 아닌 직접 정의한 데이터로 바꿔서 표현하고 싶은 경우
ticks = ['1번학생', '2번학생', '3번학생']
labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키

plt.bar(labels, values)
plt.xticks(labels, ticks, rotation = 90)