'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
    사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    힌트) 정규표현식, 문자열 색인, replace(old, new)  메서드 이용 

    주민번호 형식 : 숫자6자리-숫자1자리숫자6장리
        - 다음에 오는 숫자1(성별) : [1-4]     

    <출력 예시> 
kim 750905-*******
lee 850905-*******
park 770210-*******  
'''

import re # 정규표현식 패키지 임포트
# re.findall, re.compile, re.match 중 하나 이용 

person = """kim 750905-2049118
lee 850905-1059119
choi 790101-5142142
park 770210-1542001"""


# 방법 1 : re.match 

person = """kim 750905-2049118
lee 850905-1059119
choi 790101-5142142
park 770210-1542001"""

for p in person.split(sep='\n') : 
    result = re.match('^[a-z]{3,}\s\d{6}-[1-4]\d{6}', p)
    if result:
        print(p.replace(p[-7:],'*'*7))


################################################    

# 방법 2 : re.findall 

for p in person.split('\n') : 
    result = re.findall('\d{6}-[1-4]\d{6}', p)
    
    if result :
        print(p.replace(p[-7:],'*'*7))
################################################

# 방법 3 : re.compile + re.findall

person = """kim 750905-2049118
lee 850905-1059119
choi 790101-5142142
park 770210-1542001"""

pat = re.compile('\d{6}-[1-4]\d{6}')

for p in person.split('\n') : 
    result = re.findall(pat, p)
    if result : 
        print(p.replace(p[-7:],'*'*7))