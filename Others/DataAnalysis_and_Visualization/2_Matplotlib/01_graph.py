"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-29 02:55:33 ~ 03:05:22
"""

'''
Matplotlib
: 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리
'''

import matplotlib.pyplot as plt

'''
1. 그래프 기본
'''

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.show()

'''
Title 설정
'''

# 영어

plt.plot(x, y)
plt.title('Line Graph')
plt.show()

##############
# 한글 깨짐 현상 해결
##############

# 한국어
plt.plot(x, y)
plt.title('꺾은 선 그래프')
plt.show()
# 한글 폰트 설정 하지 않으면 한글 깨짐

'''
한글 폰트 설정
'''
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15

# 사용가능한 폰트 확인
import matplotlib.font_manager as fm
fm.fontManager.ttflist
[f.name for f  in fm.fontManager.ttflist]

# 설정완료 후 다시 plot 하면 한글 깨짐 없이 출력 됨

###################
# 음수 표기 '-' 깨짐 현상 해결
###################

plt.plot([-1, 0, 1], [-5, -1, 2])

matplotlib.rcParams['axes.unicode_minus'] = False
# 설정완료 후 다시 plot 하면 깨짐 없이 - 출력 됨