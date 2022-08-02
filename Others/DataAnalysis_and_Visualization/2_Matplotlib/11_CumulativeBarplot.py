"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-02 04:10:52 ~ 04:17:02
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd

'''
11. 누적 막대 그래프
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
plt.bar(df['이름'], df['국어'])
plt.bar(df['이름'], df['영어'])
# 그래프가 겹쳐져 있어, 누적형으로 바꿀 필요가 있음

plt.bar(df['이름'], df['국어'])
plt.bar(df['이름'], df['영어'], bottom=df['국어'])
# 국어 점수 먼저 쌓고, 그 위에 영어 점수가 나오도록 설정

plt.bar(df['이름'], df['국어'], label='국어')
plt.bar(df['이름'], df['영어'], bottom=df['국어'], label='영어')
plt.bar(df['이름'], df['수학'], bottom=df['국어']+df['영어'], label='수학')

plt.xticks(rotation=60)
plt.legend()

