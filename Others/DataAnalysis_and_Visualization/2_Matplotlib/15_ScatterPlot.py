"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-05 04:53:06 ~ 05:04:23
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd
import numpy as np
'''
15. 산점도 그래프
'''

df = pd.read_excel('score.xlsx')
df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]

'''
기존 데이터에 학년 컬럼 추가 

  지원번호   이름   학교    키   국어   영어   수학  과학  사회        SW특기  학년
0   1번  채치수  북산고  197   90   85  100  95  85      Python   3
1   2번  정대만  북산고  184   40   35   50  55  25        Java   3
2   3번  송태섭  북산고  168   80   75   70  80  75  Javascript   2
3   4번  서태웅  북산고  187   40   60   70  75  80         NaN   1
4   5번  강백호  북산고  188   15   20   10  35  10         NaN   1
5   6번  변덕규  능남고  202   80  100   95  85  80           C   3
6   7번  황태산  능남고  188   55   65   45  40  35      PYTHON   2
7   8번  윤대협  능남고  190  100   85   90  95  95          C#   2
'''

plt.scatter(df['영어'], df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

sizes = np.random.rand(8) * 1000
sizes
# 각 데이터의 point 크기가 다르게 나올 수 있도록 랜덤 값을 사이즈로 지정

plt.scatter(df['영어'], df['수학'], s=sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

# 학년 별로 데이터 표시되는 크기를 다르게 설정
sizes = df['학년']*500  # 1학년 500 / 2학년 1000 / 3학년 1500
plt.scatter(df['영어'], df['수학'], s=sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

# 학년 별로 색상도 다르게 설정
'''
https://matplotlib.org/stable/tutorials/colors/colormaps.html
위의 사이트에서 색상 지정 가능
'''
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.6)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

# Colorbar를 통해 어떤 데이터가 어떤 학년인지 확인 할 수 있음
plt.figure(figsize=(7, 7))
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.6)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks=[1, 2, 3], label='학년', shrink=0.5, orientation='horizontal')
# ticks : 컬러바의 데이터 간격을 지정
# shrink : 컬러바의 사이즈
# orientation : 컬러바 위치 및 방향
plt.show()
