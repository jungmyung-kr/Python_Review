"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-02 03:58:10 ~ 04:05:02
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

'''
막대 그래프 (심화)
'''
# 가로 그래프 화
labels = ['강백호', '서태웅', '정대만']  # 이름
values = [190, 187, 184]  # 키

plt.barh(labels, values)

# x축 값 범위 조정
plt.xlim(175, 195)

# 바의 패턴 지정
'''
https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html
위의 링크에서 다른 패턴 예시 확인  할 수 있음
'''

bar = plt.bar(labels, values)
bar[0].set_hatch('/')  # ////
bar[1].set_hatch('x')  # xxx
bar[2].set_hatch('.')  # ...

# 막대 별로 값 나타내기
bar = plt.bar(labels, values)
plt.ylim(175, 195)
for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height()+0.5, values[idx], ha='center', color='blue')
    # + 0.5 = 막대 바와 텍스트 간의 거리 조정
    # ha = 각 바 위에 텍스트의 가로 위치 ex) 가운데