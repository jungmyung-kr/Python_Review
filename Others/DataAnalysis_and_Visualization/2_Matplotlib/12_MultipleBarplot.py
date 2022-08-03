"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-03 04:17:03 ~  04:28:36
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd
import numpy as np

'''
12. 다중 막대 그래프
'''

df = pd.read_excel('score.xlsx')
df

np.arange(5)  # array([0, 1, 2, 3, 4])
np.arange(3, 6)  # array([3, 4, 5])
arr = np.arange(5)
arr + 100  # array([100, 101, 102, 103, 104])
arr * 3  # array([ 0,  3,  6,  9, 12])

######################################################

df.shape  # (8, 10) : 행과 열의 갯수를 보여줌.
df.shape[0]  # 행의 수가 곧 학생의 수이므로 0번째인 행의 정보를 가져오면 됨.

N = df.shape[0]
N
index = np.arange(N)  # 학생 수에 맞게 인덱스 설정
index  # array([0, 1, 2, 3, 4, 5, 6, 7])

w = 0.25
plt.bar(index - w, df['국어'])
plt.bar(index, df['영어'])
plt.bar(index + w, df['수학'])
# 그래프가 너무 겹쳐있어서 보기 힘듬

######################################################

w = 0.25
plt.bar(index - w, df['국어'], width=w)
plt.bar(index, df['영어'], width=w)
plt.bar(index + w, df['수학'], width=w)
# 겹치지 않게 각 막대별 두께도 얇게 설정해줌

######################################################

w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
# 범례 표시

######################################################

plt.figure(figsize=(10, 5))  # 그래프 사이즈 조정
plt.title('학생별 성적')  # 그래프 제목 설정
w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=60)  # 인덱스별로 이름 컬럼에 있는 데이터 표시
plt.show()