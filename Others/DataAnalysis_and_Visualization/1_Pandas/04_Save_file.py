"""
https://www.youtube.com/watch?v=PjhlUzp_cU0&t=960s

나도코딩
파이썬 코딩 무료 강의 (활용편5) - 데이터 분석 및 시각화, 이 영상 하나로 끝내세요

2022-07-25 00:35:25 ~ 00:53:24
"""

'''
파일 저장 및 열기
: DataFrame 객체를 excel, csv, txt로 저장 및 열기
'''

import pandas as pd

data = {
    '이름': ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교': ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키': [197, 184, 168, 187, 188, 202, 188, 190],
    '국어': [90, 40, 80, 40, 15, 80, 55, 100],
    '영어': [85, 35, 75, 60, 20, 100, 65, 85],
    '수학': [100, 50, 70, 70, 10, 95, 45, 90],
    '과학': [95, 55, 80, 75, 35, 85, 40, 95],
    '사회': [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기': ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
df.index.name = '지원번호'


######################################################

'''
저장하기
: csv 파일로 저장
'''

df.to_csv('score.csv', encoding='utf-8-sig')

# 만약 인덱스 값을 빼고 싶다면
df.to_csv('score.csv', encoding='utf-8-sig', index=False)

'''
텍스트 파일로 저장
'''
df.to_csv('score.txt', sep='\t')

'''
엑셀 파일로 저장
'''
df.to_excel('score.xlsx')

######################################################

'''
열기
csv 파일 열기
'''

df = pd.read_csv('score.csv')

# 일부 행은 제외하고 불러오고 싶다면

# 1. 지정된 갯수 만큼의 row를 건너뜀
# : 2행까지 건너뛰고 3행부터 불러오기
df = pd.read_csv('score.csv', skiprows=2)
df

# 2. 일부 row 제외
# : 1,3,5행 제외하고 불러오기
df = pd.read_csv('score.csv', skiprows=[1, 3, 5])
df

# 3. 지정된 갯수만큼 row 가져오고 싶다면
df = pd.read_csv('score.csv', nrows=5)
df

# 4. 처음 2 row 무시, 그 후 4개 row 가져오기
# cf. skiprow하면 컬럼명들로 이뤄진 행도 그 중에 포함됨
df = pd.read_csv('score.csv', skiprows=2, nrows=5)
df

'''
텍스트 파일 열기
'''
df = pd.read_csv('score.txt', sep='\t')
df

# 자동 인덱스 제외하고 기존 컬럼 중 하나로 인덱스 변경
# 방법 1
df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')
df

# 방법 2
df = pd.read_csv('score.txt', sep='\t')
df.set_index('지원번호', inplace=True)
df

'''
엑셀 파일 열기
'''
df = pd.read_excel('score.xlsx')
df

# 자동 인덱스 제외하고 기존 컬럼 중 하나로 인덱스 변경
df = pd.read_excel('score.xlsx', index_col='지원번호')
df