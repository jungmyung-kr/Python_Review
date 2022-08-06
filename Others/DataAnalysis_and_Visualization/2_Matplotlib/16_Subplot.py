"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-06 05:04:24 ~ 05:13:17
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd
import numpy as np
'''
16. 여러 그래프
'''

df = pd.read_excel('score.xlsx')
df
'''
 지원번호   이름   학교    키   국어   영어   수학  과학  사회        SW특기
0   1번  채치수  북산고  197   90   85  100  95  85      Python
1   2번  정대만  북산고  184   40   35   50  55  25        Java
2   3번  송태섭  북산고  168   80   75   70  80  75  Javascript
3   4번  서태웅  북산고  187   40   60   70  75  80         NaN
4   5번  강백호  북산고  188   15   20   10  35  10         NaN
5   6번  변덕규  능남고  202   80  100   95  85  80           C
6   7번  황태산  능남고  188   55   65   45  40  35      PYTHON
7   8번  윤대협  능남고  190  100   85   90  95  95          C#
'''
######## 여러 그래프 나열할 공간 생성

fig, axs = plt.subplots(2, 2, figsize=(15, 10))  # 2 X 2에 해당하는 plot 들을 생성
fig.suptitle('여러 그래프 넣기')

######## 첫번째 그래프
axs[0, 0].bar(df['이름'], df['국어'], label='국어 점수')
axs[0, 0].set_title('첫번째 그래프')  # 여러개의 그래프를 나열할때는 그냥 title(X) set_title
axs[0, 0].legend()
axs[0, 0].set(xlabel='이름', ylabel='점수')
axs[0, 0].set_facecolor('lightyellow')
axs[0, 0].grid(linestyle='--', linewidth=0.5)

######## 두번째 그래프
axs[0, 1].plot(df['이름'], df['수학'], label='수학 점수')
axs[0, 1].plot(df['이름'], df['영어'], label='영어 점수')
axs[0, 1].legend()

######## 세번째 그래프
axs[1, 0].barh(df['이름'], df['키'])

######## 네번째 그래프
axs[1, 1].plot(df['이름'], df['사회'], color='green', alpha=0.5)
