"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-23 00:00:00 ~00:15:33
"""

'''
Pandas
: 파이썬에서 사용하는 데이터 분석 라이브러리
'''

import pandas as pd

'''
Series
: 1차원 데이터 (정수, 실수, 문자열 등)
'''

'''
Series 객체 생성
예) 1월부터 3월까지 평균 온도 데이터 (-20, -10, 10, 20)
'''
temp = pd.Series([-20, -10, 10, 20])
print(temp)
'''
0   -20
1   -10
2    10
3    20
dtype: int64
'''
temp[0]  # 1월 온도 : -20
temp[2]  # 3월 온도 : 10

'''
Series 객체 생성 (Index 지정)
'''
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
'''
Jan   -20
Feb   -10
Mar    10
Apr    20
dtype: int64
'''

temp['Jan']  # Index Jan에 해당하는 데이터 출력 : -20
temp['Apr']  # Index Apr에 해당하는 데이터 출력 : 20
# temp['Jun'] : Index에 없는 키를 입력하는 경우 KeyError발생