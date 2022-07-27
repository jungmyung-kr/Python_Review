"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-27 02:24:12 ~ 02:31:26
"""

import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df['학교'] = df['학교'] + '등학교'
df

df['키'] = df['키'] + 'cm'
'''
'add' did not contain a loop with signature matching types 
(dtype('int64'), dtype('<U2')) -> None

위의 학교 + 등학교와 달리, (문자열 + 문자열) 
키 컬럼의 데이터는 정수형 / 추가하려고 하는 cm는 문자열 
따라서 둘의 형식을 맞춰 주지 않으면 에러 발생
'''

######################################################

'''
데이터에 함수 적용 (Apply)
'''
###################
# 키 뒤에 cm 붙이는 역할
###################


def add_cm(height):
    return str(height) + 'cm'


df['키'] = df['키'].apply(add_cm)
df
'''
      이름      학교      키   국어   영어   수학  과학  사회        SW특기
지원번호                                                       
1번    채치수  북산고등학교  197cm   90   85  100  95  85      Python
2번    정대만  북산고등학교  184cm   40   35   50  55  25        Java
3번    송태섭  북산고등학교  168cm   80   75   70  80  75  Javascript
4번    서태웅  북산고등학교  187cm   40   60   70  75  80         NaN
5번    강백호  북산고등학교  188cm   15   20   10  35  10         NaN
6번    변덕규  능남고등학교  202cm   80  100   95  85  80           C
7번    황태산  능남고등학교  188cm   55   65   45  40  35      PYTHON
8번    윤대협  능남고등학교  190cm  100   85   90  95  95          C#
'''

#######################################
# SW 특기 첫 글자만 대문자로, 나머지는 소문자로 만드는 역할
#######################################

# 방법 1 :


def sw_capitalize(lang):
    if pd.notnull(lang):
        return lang.capitalize()
    else:
        return lang


df['SW특기'] = df['SW특기'].apply(sw_capitalize)
df
'''
      이름      학교      키   국어   영어   수학  과학  사회        SW특기
지원번호                                                       
1번    채치수  북산고등학교  197cm   90   85  100  95  85      Python
2번    정대만  북산고등학교  184cm   40   35   50  55  25        Java
3번    송태섭  북산고등학교  168cm   80   75   70  80  75  Javascript
4번    서태웅  북산고등학교  187cm   40   60   70  75  80         NaN
5번    강백호  북산고등학교  188cm   15   20   10  35  10         NaN
6번    변덕규  능남고등학교  202cm   80  100   95  85  80           C
7번    황태산  능남고등학교  188cm   55   65   45  40  35      Python
8번    윤대협  능남고등학교  190cm  100   85   90  95  95          C#
'''

# 방법 2

df['SW특기'].str.capitalize()