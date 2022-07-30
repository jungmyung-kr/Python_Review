"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-29 03:15:56 ~ 03:35:47
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

######################################################

'''
4. 스타일
'''

######################################################

# 마커
'''
https://matplotlib.org/stable/api/markers_api.html
사용 가능한 마커들 확인할 수 있음.

ex)
o : circle
v : triangle_down
^ : triangle_up
s : square
'''

plt.plot(x, y, marker='o')
plt.plot(x, y, marker='X')

# 마커 사이즈
plt.plot(x, y, marker='v', markersize='10')
# 마커 테두리 색상
plt.plot(x, y, marker='X', markersize=20, markeredgecolor='red')
# 마커 색상
plt.plot(x, y, marker='X', markersize=20,\
         markeredgecolor='red', markerfacecolor='yellow')

######################################################

# 선
'''
https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
사용 가능한 선 스타일 확인할 수 있음

ex) 
'-'	solid line style

https://matplotlib.org/stable/gallery/color/named_colors.html
사용 가능한 선 색 확인할 수 있음

ex) 
<Base Colors>
b : blue
g : grean
r : red

<CSS Colors>
tomato
darkorange
gold
forestgreen
dodgerblue
....
'''

# 선 굵기
plt.plot(x, y, linewidth=5)

# 선 스타일
plt.plot(x, y, linestyle=':')  # 점선
plt.plot(x, y, linestyle='--')  # 보다 굵고 긴 점선
plt.plot(x, y, linestyle='-.')  # 선과 점 반복되는 스타일

# 선 색깔
plt.plot(x, y, color='pink', linewidth=5)
plt.plot(x, y, color='b')
plt.plot(x, y, color='#ff0000')  # rgb값으로도 가능

######################################################

'''
포맷

plt.plot( x, y, 'color, marker, linestyle')
'''

plt.plot(x, y, 'ro--')
plt.plot(x, y, 'bv:')
plt.plot(x, y, 'go')

######################################################

'''
축약어

ex)

linestyle or ls
linewidth or lw
markeredgecolor or mec
markeredgewidth or mew
markerfacecolor or mfc
markersize or ms
'''

plt.plot(x, y, marker='o', mfc='gold', ms=10, mec='forestgreen', ls=":")

######################################################

'''
투명도

(0~1)사이의 수치

강조하고 싶은 데이터는 1로 두고 
그 외 데이터는 투명도를 낮추는 등으로 사용 가능
'''
plt.plot(x, y, marker='o', mfc='red', ms=10, alpha=0.3)

######################################################

'''
그래프 크기
'''

plt.figure(figsize=(10, 5))
plt.plot(x, y)

plt.figure(figsize=(10, 5), dpi=150)  # dpi (dots per inch) : 확대
plt.plot(x, y)

######################################################

'''
배경색
'''

plt.figure(facecolor='#a1c3ff')
plt.plot(x, y)