"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-04 04:38:44 ~ 04:50:05
2022-08-05 04:50:06 ~ 04:53:05
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd
'''
14. 원 그래프 (심화)
'''

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'ETC']
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()

######################################################

# 색상 변경
# colors = ['b', 'g', 'r', 'c', 'm', 'y']

colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
explode = [0.05] * 6
plt.pie(values, labels=labels, autopct='%.1f%%',\
        startangle=90, counterclock=False, colors=colors, explode=explode)
plt.show()

######################################################

# 속성 설정 ( 도넛형 그래프, edge 색상 등..)

wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':2}
# width : 도넛 그래프 두께
# edgecolor
# linewidth

plt.pie(values, labels=labels, autopct='%.1f%%',\
        startangle=90, counterclock=False, colors=colors,\
        explode=explode, wedgeprops=wedgeprops)
plt.show()


# 10% 이상의 데이터만 수치 나타나게 설정 (소수점 없이 정수만)
def custom_autopct(pct):
    # return ('%.1f%%' % pct) if pct >= 10 else '' : 아래와 같은 표현 방식
    return '{:.0f}%'.format(pct) if pct >= 10 else ''


plt.pie(values, labels=labels, autopct=custom_autopct,\
        startangle=90, counterclock=False, colors=colors,\
        explode=explode, wedgeprops=wedgeprops, pctdistance=0.7)
plt.show()
# pctdistance = 글씨 중심에서 이동


'''
DataFrame 활용
'''
df = pd.read_excel('score.xlsx')
df

grp = df.groupby('학교')
grp

grp.size()['북산고']  # 5
grp.size()['능남고']  # 3

values = [grp.size()['북산고'], grp.size()['능남고']]  # [5, 3]
labels = ['북산고', '능남고']

plt.pie(values, labels=labels)
plt.title('소속 학교')
plt.show()