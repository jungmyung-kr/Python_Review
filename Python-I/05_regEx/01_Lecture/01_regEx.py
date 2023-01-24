"""
chap05_regExText
step01_regEx.py
"""

'''
정규 표현식(Regular Expressions)  
    - 특정한 규칙을 가진 메타문자를 이용하여 패턴을 지정한 문자열 표현 

[주요 메타문자]
.x : 임의의 한 문자 뒤에 x가 오는 문자열(예 : abc, mbc -> .bc) 
x. : x 다음에 임의의 한 문자가 오는 문자열(예 : t1, t2, ta -> t.) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x* : x가 0번 이상 반복(없는 경우 포함)
x+ : x가 1회 이상 반복
x? : x가 0 또는 1회 포함 
x{m, n} : x가 m~n 사이 연속 
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
[^x] : x문자 제외 
| : or 조건식(예 : [a-z|A-Z] -> 영문자 소문자 또는 대문자) 
\ : 이스케이프 문자 또는 일반문자를 메타문자로 인식(예: \d, \w, \s)
() : 그룹핑(예 : '([a-z]{3}|\d{3})' -> -> 영문자 3자 연속 또는 숫자 3자 연속)
'''

st1 = '1234 abc홍길동 ABC_555_6 알베르토'
st2 = 'test1abcABC 123mbc abbc,ac 45text'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

'''
모듈(module) : 함수 또는 클래스를 포함한 파이썬 파일
'''

# 정규표현식과 문자열 처리 함수 제공 모듈 

import re # 모듈(re.py) - 방법1 
# import 모듈명
# re.findall(pattern, string)

from re import findall, match, sub, search # 방법2(권장)
# from 모듈명 import 함수1, 함수2, 함수3
# findall(pattern, string)
# 앞처럼 re.호출  안해도 돼서 이 방법 권장하는 듯
# re 모듈의 함수 : findall(), match(), sub()

from re import * # 방법3 

# 1. re.findall('pattern', string) 
# 패턴과 일치하는 문자열 찾기 -> list 반환 

# 1) 숫자(\d) 찾기  : [x] : x 1개, {n} : n 연속 
print(re.findall('1234', st1)) # ['1234']
print(re.findall('[0-9]', st1)) # ['1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall('[0-9]{3}', st1)) # ['123', '555']
print(re.findall('[0-9]{3,4}', st1)) # ['1234', '555']
print(re.findall('\d{3,4}', st1)) # ['1234', '555'] 위랑 같음. 

# 2) 문자열 찾기 
print(findall('[가-힣]{3}', st1)) #['홍길동', '알베르'] {3}: 3자 
print(findall('[가-힣]{3,}', st1)) #['홍길동', '알베르토'] 위와의 차이: 콤마, {3,} : 3자 이상 
print(findall('[a-z]{3}', st1)) # ['abc']
print(findall('[a-z|A-Z]{3}', st1)) # | : or조건  ['abc', 'ABC']


st1 # '1234 abc홍길동 ABC_555_6 알베르토'
type(st1) # str

words = st1.split() # 공백 기준 단어 
words # ['1234', 'abc홍길동', 'ABC_555_6', '알베르토']

names = [] # 한글 이름 저장 
for word in words :
    result = findall('[가-힣]{3,}', word) # 3자 이상 한글 단어 찾아서 result 저장
    print(result) # []
    if result : # False  = [], True = ['홍길동'] not null([])
        names.extend(result) # ['홍길동']
print(names) # ['홍길동', '알베르토']
'''
names = [] # 한글 이름 저장 
for word in words :
    result = findall('[가-힣]{3,}', word)
    print(result) # []
여기까지만 하면 이렇게 출력됨.
-> 패턴과 일치하지 않으면 [] null = 빈칸으로 / 일치하면 []안에 반환
[] -> '1234' 중에 패턴에 일치하는 것 없음
['홍길동'] -> 'abc홍길동' 중에 일치하는 '홍길동'만 출력
[]
['알베르토']

패턴에 일치하는 것만 모아서 리스트 만들려면 추가 작업 필요. 

if result : # False  = [], True = ['홍길동'] not null([])
    names.extend(result) # ['홍길동']
    이부분 추가해야함. 
(파이썬은 값이 없는 것을 false 취급)
'''


# 3) 접두어/접미어 문자열 찾기 
st2 = 'test1abcABC 123mbc abbc,ac 45text'

print(findall('^test', st2)) # ['test']
print(findall('^text', st2)) # [] : text로 시작하는 것 찾기 -> 45text의 text 안나옴
print(findall('text$', st2)) # ['text']

# 문자열 중간에서 찾기 : . 메타문자 
print(findall('.bc', st2)) # ['abc', 'mbc', 'bbc']
print(findall('b.', st2)) # ['bc', 'bc', 'bb']


# [문제] 'http://news'로 시작하는 url 추출하기  
urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']
len(urls) # 4 

result = [] # 올바른 url 저장하기 위한 빈 list

for url in urls :
    result = findall('^http://news', url)
    if result : 
        print(url)

'''
print(result)가 아니라 result가 true 값인 애들의 url을 출력하라고 해야함
안그러면 그 접두어만 출력됨 
http://news.com/test
http://news.com/test2
'''


# url 추출 : startswith() 이용 
for url in urls :
    if url.startswith('http://news') :
        print(url)
    

# 4) 단어(word)  :  \w - 한글,영문,숫자(특수문자, 문장부호, 공백 제외)  
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\w{3,}', st3)
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']
# 불용어(ex.특문) 제외하고 저장하려할 때 쓸 수 있는 기능


# 5) 문자열 제외 : [^제외문자]
print(findall('[^t]+', st3)) # # t제외한 나머지 문자 1개 이상(+) 연속 문자 반환  
# ['es', '^홍길동 abc 대한*민국 123$', 'bc']

# 불용어 : 특수문자, 공백 제외 : '^', '*', '$', ' '(\s)
print(findall('[^^*$\s]+', st3)) # 불용어 제거 후 1개 이상 연속 문자 반환 
# ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']


# 6) x문자 반복 :  ., *, +, ?
st2 # 'test1abcABC 123mbc abbc,ac 45text'

# x가 0번 이상 반복 : *
findall('ab*c', st2) 
# ab*c : b가 한번도 안나오는 경우, 한번 나오는 경우, 그 이상 나오는 경우 
# ['abc', 'abbc', 'ac']

# x가 1회 이상 반복 : + 
print(findall('ab+c', st2)) 
# ab+c : b가 적어도 1번 이상은 나오는경우
# ['abc', 'abbc']

# x? : x가 0 또는 1회 포함 
print(findall('ab?c', st2)) 
# ab?c : b가 한번도 안나오거나 한번만 나오거나
# ['abc', 'ac']


####################################################################################


# 2. re.match(pattern, string) 
# 패턴 일치 여부 반환 : 일치 -> object 반환, 불일치 -> NULL 반환 

# 패턴 일치 예시
jumin = '123456-3234567'
type(jumin) # str 

result = match('\d{6}-[1-4]\d{6}', jumin) # match 객체 반환 
print(result) # <re.Match object; span=(0, 14), match='123456-3234567'>

# 패턴 불일치 예시 
jumin = '123456-5234567'
result = match('\d{6}-[1-4]\d{6}', jumin) # match 객체 반환 
print(result) # None = NULL 



if result : # true = object
    print('주민번호 양식')
    print('주민번호 :', result.group()) # 일치된 내용 추출 
else :
    print('잘못된 양식')

# 매칭된 텍스트 반환
result.group() # '123456-3234567'
# .group() : 개당 객체 안에 매칭된 텍스트들만 보여줌 




####################################################################################

# 3. re.sub(pattern, rep, string) # gsub() 유사함 
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text = sub('[\^*$]', '', st3) # '[\^\*\$]'
#sub('지울 단어','대체단어', 대상)
# 대체 단어에 ''이렇게 따옴표만 기입하면 -> 제거 
# ^ 자체가 메타문자이므로 
# 그냥 ^라고 쓰면 *$로 시작하는 단어들을 찾게 됨.
# ^*$라는 특문을 지우고 싶은거면 앞에 \를 달아주어야 메타가 아닌 특문으로 인식함

print(text) # test홍길동 abc 대한민국 123tbc

# sub vs findall
sub('[\^*$\s]','',st3) # 교체(제거)
#'test홍길동abc대한민국123tbc'
# 원본을 유지하면서 불필요한 불용어만 제거해줌 

findall('[^^*$\s]+', st3) # 찾기
# ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']
# 불용어를 제거하고 나머지를 단어 집합으로 추출 

####################################################################################

# 4. re.search(pattern, string)

text = "<span> <head> 안녕하세요. </head> </span>"
head = search("<head.*</head>", text) # . : >, * : 
head.group() # '<head> 안녕하세요. </head>'

text2 = "<span> <head></head> </span>"
head2 = search("<head>.+</head>", text2)
head2.group() # '<head> 안녕하세요. </head>'
# AttributeError: 'NoneType' object has no attribute 'group'
# .*는 0번 이상 출현 패턴이라 내부에 아무런 글이 없어도 문제가 없지만
# .+ 임의의 문자 '1'번 이상 이라서 아무것도 없는 경우 패턴을 찾기가 불가능 => 에러


'''
--------------------------------------------------
.:임의의 문자 하나
*:해당 문자 0번 이상 출현하는 패턴
.*: 임의의 문자 0번 이상 출현 패턴
=> 이 경우 <head뒤의 '> 안녕하세요. '가 대상이 됨.
--------------------------------------------------
.+: 임의의 문자 1번 이상 출현 패턴
'''
####################################################################################

# 5. re.compile(pattern) : 패턴 객체 생성 -> 반복 사용 
urls = ['http://news.com/test', 'new.com', 'http://news.com/test2', 'http//~']
print(urls) # ['http://news.com/test', 'new.com', 'http://news.com/test2', 'http//~']

# 올바른 urls 추출 
url_pat = re.compile('http://news')
dir(url_pat) # 사용할 수 있는 메서드 조회
# findall

# findall() : 일치된 내용 반환
url_pat.findall(urls[0]) # ['http://news'] -> True
url_pat.findall(urls[1]) # [] -> False


for url in urls :
    if url_pat.findall(url) : # 패턴 반복 사용 
        print(url)

'''
http://news.com/test
http://news.com/test2
'''

# list 내포 
urls_re = [url for url in urls if url_pat.findall(url)] 
print(urls_re)