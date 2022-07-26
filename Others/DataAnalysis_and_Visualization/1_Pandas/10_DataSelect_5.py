"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-25 01:34:13 ~ 01:43:37
"""

'''
데이터 선택 (조건)
: 조건에 해당 하는 데이터 선택
'''

import pandas as pd

df = pd.read_excel('score.xlsx', index_col='지원번호')
df

'''
str함수
'''
filt = df['이름'].str.startswith('송')  # 송씨 성을 가진 사람
df[filt]
'''
       이름   학교    키  국어  영어  수학  과학  사회        SW특기
지원번호                                               
3번    송태섭  북산고  168  80  75  70  80  75  Javascript
'''

filt = df['이름'].str.contains('태')  # 이름에 '태'가 들어가는 사람
df[filt]
'''
       이름   학교    키  국어  영어  수학  과학  사회        SW특기
지원번호                                               
3번    송태섭  북산고  168  80  75  70  80  75  Javascript
4번    서태웅  북산고  187  40  60  70  75  80         NaN
7번    황태산  능남고  188  55  65  45  40  35      PYTHON
'''

df[~filt]  # # 이름에 '태'가 들어가는 사람 제외
'''
       이름   학교    키   국어   영어   수학  과학  사회    SW특기
지원번호                                              
1번    채치수  북산고  197   90   85  100  95  85  Python
2번    정대만  북산고  184   40   35   50  55  25    Java
5번    강백호  북산고  188   15   20   10  35  10     NaN
6번    변덕규  능남고  202   80  100   95  85  80       C
8번    윤대협  능남고  190  100   85   90  95  95      C#
'''

langs = ['Python', 'Java']
filt = df['SW특기'].isin(langs)
df[filt]
'''
       이름   학교    키  국어  영어   수학  과학  사회    SW특기
지원번호                                            
1번    채치수  북산고  197  90  85  100  95  85  Python
2번    정대만  북산고  184  40  35   50  55  25    Java

* 대문자로 기입된 7번 학생은 가져오지 못함
7번    황태산  능남고  188  55  65  45  40  35      PYTHON
'''

langs = ['python', 'java']
filt = df['SW특기'].str.lower().isin(langs)
df[filt]
'''
       이름   학교    키  국어  영어   수학  과학  사회    SW특기
지원번호                                            
1번    채치수  북산고  197  90  85  100  95  85  Python
2번    정대만  북산고  184  40  35   50  55  25    Java
7번    황태산  능남고  188  55  65   45  40  35  PYTHON
'''


# Java라는 글자가 들어간 sw 모두 출력하기

filt = df['SW특기'].str.contains('Java')
'''
위의 str.lower()의 경우 문제가 없었는데 str.contains는 오류 발생.
ValueError: Cannot mask with non-boolean array containing NA / NaN values

일부 데이터가 비어있기 때문에(NaN) contains을 하는지 확인해줄 수 없음

df['SW특기'].str.contains('Java')

출력결과
:
지원번호
1번    False
2번     True
3번     True
4번      NaN <-
5번      NaN <-
6번    False
7번    False
8번    False
Name: SW특기, dtype: object

따라서 NaN 부분을 어떻게 처리할 지 규정해줘야 함
na = True / na = False
'''

filt = df['SW특기'].str.contains('Java', na=True)  # NaN(비어있는 데이터)를 True로 처리
'''
지원번호
1번    False
2번     True
3번     True
4번     True <-
5번     True <-
6번    False
7번    False
8번    False
Name: SW특기, dtype: bool
'''

filt = df['SW특기'].str.contains('Java', na=False)
'''
지원번호
1번    False
2번     True
3번     True
4번    False <-
5번    False <-
6번    False
7번    False
8번    False
Name: SW특기, dtype: bool
'''

df[filt]
'''
       이름   학교    키  국어  영어  수학  과학  사회        SW특기
지원번호                                               
2번    정대만  북산고  184  40  35  50  55  25        Java
3번    송태섭  북산고  168  80  75  70  80  75  Javascript
'''