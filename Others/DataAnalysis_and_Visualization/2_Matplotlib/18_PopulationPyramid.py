"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-08-08 05:27:16 ~ 05:37:54

"""
'''
인구 피라미드

자료 출처 : https://jumin.mois.go.kr/ageStatMonth.do#none
연령별 인구현황 2012년 7월 만 0세~ 만 100세 이상의 전국 인구 수 데이터
'''

import pandas as pd
df_m = pd.read_excel('201207_201207_연령별인구현황_월간.xlsx',\
                     skiprows=3, index_col='행정기관', usecols='B, E:Y')
# skiprows : 위의 3개의 줄 무시
# index_col : 전체 열 중에 행정 기관 열의 데이터들을 인덱스로 사용
# usecols : 남자용 데이터만 선택할 수 있게 필요한 열만 지정

df_m.head(3)
