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

######################################################

# 남자 데이터 정의

df_m = pd.read_excel('201207_201207_연령별인구현황_월간.xlsx',\
                     skiprows=3, index_col='행정기관', usecols='B, E:Y')
# skiprows : 위의 3개의 줄 무시
# index_col : 전체 열 중에 행정 기관 열의 데이터들을 인덱스로 사용
# usecols : 남자용 데이터만 선택할 수 있게 필요한 열만 지정

df_m.head(3)
'''
             0~4세       5~9세     10~14세  ...  90~94세 95~99세 100세 이상
행정기관                                      ...                       
전국       1,198,690  1,206,194  1,585,781  ...  24,531  5,004   2,818
서울특별시      216,282    209,976    273,943  ...   4,984  1,235     956
부산광역시       67,983     68,448     96,547  ...   1,235    258     248
'''

# 전국의 남성 / 여성 연령별 데이터를 시각화 하고자 함.
# 전국데이터인 0번째 행을 선택하여, 데이터들을 문자 -> 정수형으로 변경
# str중 ,를 ''으로 대체한 후, 정수형으로 변경
df_m.iloc[0] = df_m.iloc[0].str.replace(',', '').astype(int)
df_m.head(3)
'''
'전국'행의 데이터들만 ','가 제거된 것을 확인 할 수 있음.

           0~4세     5~9세   10~14세   15~19세  ...  85~89세 90~94세 95~99세 100세 이상
행정기관                                         ...                              
전국       1198690  1206194  1585781  1864217  ...   78930  24531   5004    2818
서울특별시    216,282  209,976  273,943  338,642  ...  13,514  4,984  1,235     956
부산광역시     67,983   68,448   96,547  126,217  ...   4,398  1,235    258     248
'''

######################################################

# 여자 데이터도 동일하게 준비

df_f = pd.read_excel('201207_201207_연령별인구현황_월간.xlsx',\
                     skiprows=3, index_col='행정기관', usecols='B, AB:AV')
df_f.head(3)

'''
            0~4세.1     5~9세.1   10~14세.1  ... 90~94세.1 95~99세.1 100세 이상.1
행정기관                                      ...                            
전국       1,129,941  1,121,523  1,451,920  ...   77,722   19,914     9,362
서울특별시      204,712    197,636    253,176  ...   13,622    4,062     2,797
부산광역시       64,620     63,465     86,623  ...    4,379    1,188       890
'''

df_f.columns = df_m.columns
# 여성 데이터의 컬럼명이 남성과 동일하기 때문에
# 저장할 때 0~4세.1 이런 식으로 뒤에 .1을 붙여 구분시켜줌
# 해당 부분을 다시 동일하게 만들어주는 과정

df_f.iloc[0] = df_f.iloc[0].str.replace(',', '').astype(int)
df_f.head(3)
'''
           0~4세     5~9세   10~14세   15~19세  ...  85~89세  90~94세 95~99세 100세 이상
행정기관                                         ...                               
전국       1129941  1121523  1451920  1654308  ...  213960   77722  19914    9362
서울특별시    204,712  197,636  253,176  306,004  ...  35,582  13,622  4,062   2,797
부산광역시     64,620   63,465   86,623  107,815  ...  13,697   4,379  1,188     890
'''

######################################################

'''
데이터 시각화 
'''

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, -df_m.iloc[0] // 1000)
# 남성 데이터가 여성과 겹치지 않도록, 왼쪽에 배치해주기 위해 '-'를 기입해줌
# 데이터가 커서 천 명 단위로 나눠줌
plt.barh(df_f.columns, df_f.iloc[0] // 1000)
plt.title('2012 인구피라미드')
plt.show()
plt.savefig('2012_인구피라미드.png', dpi=100)

######################################################

# 2022년 데이터도 동일한 과정으로 진행

# 남자 데이터 정의

df_m2 = pd.read_excel('202207_202207_연령별인구현황_월간.xlsx',\
                      skiprows=3, index_col='행정기관', usecols='B, AB:AV')

df_m2.head(3)
'''
          0~4세.1     5~9세.1   10~14세.1  ... 90~94세.1 95~99세.1 100세 이상.1
행정기관                                    ...                            
전국       749,841  1,107,540  1,219,290  ...   52,342    9,173     1,558
서울특별시    120,802    167,636    188,149  ...    9,269    1,858       431
부산광역시     42,859     65,865     68,969  ...    3,024      452        88
'''
df_m2.columns = df_m.columns
df_m2.iloc[0] = df_m2.iloc[0].str.replace(',', '').astype(int)
df_m2.head(3)

df_f2 = pd.read_excel('202207_202207_연령별인구현황_월간.xlsx',\
                      skiprows=3, index_col='행정기관', usecols='B, AY:BS')
df_f2.head(3)

'''
          0~4세.2     5~9세.2   10~14세.2  ... 90~94세.2 95~99세.2 100세 이상.2
행정기관                                    ...                            
전국       712,701  1,054,599  1,151,492  ...  172,735   39,353     6,975
서울특별시    113,210    160,003    178,144  ...   25,305    6,351     1,312
부산광역시     40,725     62,511     65,495  ...   10,225    2,278       346
'''

df_f2.columns = df_m2.columns
df_f2.iloc[0] = df_f2.iloc[0].str.replace(',', '').astype(int)
df_f2.head(3)

plt.figure(figsize=(10, 7))
plt.barh(df_m2.columns, -df_m2.iloc[0] // 1000)
# 남성 데이터가 여성과 겹치지 않도록, 왼쪽에 배치해주기 위해 '-'를 기입해줌
# 데이터가 커서 천 명 단위로 나눠줌
plt.barh(df_f2.columns, df_f2.iloc[0] // 1000)
plt.title('2022 인구피라미드')
plt.show()
plt.savefig('2022_인구피라미드.png', dpi=100)
