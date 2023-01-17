"""
chap02_String 
step01_string
"""

'''
문자열(string)의 특징
- 문자열: 순서가 있는 문자들의 집합
- 순서가 존재
- 인덱싱 / 슬라이싱 
- 수정 불가 : 새로운 객체 생성
'''


# 1. 문자열 유형 

# 1) 한 줄 문자열 
lineStr = "this is one line string" 
print(type(lineStr)) # <class 'str'>

# 2) 여러줄 문자열 
multiLine = """This
is multi line
string"""
print(multiLine)
print(type(multiLine)) # <class 'str'>

'''
class: 객체를 생성하는 도구
object : class에 의해서 만들어진 결과물 = 객체
'''

# 3) sql문 
query ="""select * from emp
where deptno = 1001
order by sal desc"""
print(query)


# 2. indexing/slicing 가능 

'''
R의 index : 1부터 -> 변수[1]
Python의 index : 0부터 -> 변수[0]
'''

# 1) indexing : 특정 문자 참조
# 왼쪽 기준 색인 
print(lineStr) # this is one line string
print('왼쪽의 첫번째 문자 : ', lineStr[0]) # t
print(lineStr[0:4]) # 0부터 4의 이전까지인 3까지 가져옴 : this
print(lineStr[:4]) # 위랑 같은 결과, 시작점이 첫글자면 생략 가능: this

# 오른쪽 기준 색인 
print(lineStr[-1]) # g
print(lineStr[-6:]) # string  : -6부터 끝까지
print(lineStr[-6:-1]) # strin : -6부터 -1전인 -2까지 

# 2) slicing : 특정 문자 집합 자르기 -> new object
subStr = lineStr[:4]
print(subStr) # this

print(id(lineStr)) # 2063029382880
print(id(subStr)) # 2063057380208
# subStr이 lineStr에서 추출한 거지만 아예 다른 위치에 저장되어 있음을 확인 가능

# 3. 문자열 연산 


print('python' + ' program') # 결합연산자 

print('-'*50) # 반복연산자 


# 4. 문자열 처리 함수 

# 형식) 스트링객체.메서드()

testStr = " My name is hong!! "  # 스트링객체
print(type(testStr)) # <class 'str'>
len(testStr) # 19

dir(testStr) # 스트링객체(문자열) 메서드(함수) 확인  
'''
많은데 일부만 
'count',
'find',
'index',
'isnumeric',
'lower',
'replace',
'split',
'strip',
'upper',
'''

# 1) 문자 찾기 
# 주어진 문자열이 없음 : -1 반환
# 주어진 문자열이 있음 : 해당 문자열 위치(색인,index) 반환 

print(testStr.find('z')) # -1: z 없다 
print(testStr.find('m')) # 6
print(testStr.find('M')) # 1 
print(testStr.index('B')) # ValueError: substring not found
print(testStr.index('is')) # 9
'''
find() : 색인 반환, 문자 없는 경우(-1)
index() : 색인 반환, 문자 없는 경우(error)
'''

# 2) 문자 개수 반환  
print(testStr.count('n')) # 2

# 3) 문자 유형 구분 
testStr.isalpha() # 순수하게 알파벳으로 구성되었는지? : False (공백, 숫자, 특문 포함한다)  
testStr.isascii() # 아스키 코드로만 구성되었는가 : True (영문자, 공백, 숫자, 특문) 
# False: ex) 한글 포함 
# 아스키 코드 : 영어로만 된 키보드 생각해보길 / 한글은 유니코드 
testStr.islower() # 순수하게 소문자로만 구성되었는지? : False
"1234".isnumeric() # 모든 구성요소가 숫자인가? : True

# 4) 대소문 처리 
testStr.upper() # ' MY NAME IS HONG!! '
testStr.lower() # ' my name is hong!! '

# 5) 접두어 판단 -> T/F
testStr.startswith(' My') # True
testStr.startswith('My') # False : 공백도 문자에 포함됨

testStr.strip() 
# 문장의 앞뒷 공백 제거, 그러나 testStr 객체의 내용이 수정되는 건 아님.
# 만약에 공백 제거 하고 저장하고 싶다면 새로운 변수명 앞에 달아줘야
newTestStr=testStr.strip() # 'My name is hong!!'

newTestStr.startswith('My') # True
# 앞 공백 지워서 새로 만들고 조회하니 이번엔 True

# 6) 단어 교체 
testStr = testStr.replace('!', '')
testStr # ! 제거 : ' My name is hong '
len(testStr) # 17

testStr = testStr.replace(' ','')
testStr # 공백 제거: 'Mynameishong'
len(testStr) # 12
testStr.isalpha() # True


# 5. 문자열 분리(split) & 결합(join)
'''
split : 문단 -> 문장 or 문장 -> 단어
join: 단어 -> 문장
'''

print(multiLine)
'''
This
is multi line
string
'''

# 1) split : 문자열 분리
# 문단 -> 문장 split

sents = multiLine.split(sep='\n')
print(sents) # ['This', 'is multi line', 'string']
len(sents) # 3

'''
함수(function) vs 메서드(method)
- 공통점 : 기능 제공
- 차이점 : 함수(단독), 메서드(객체에 의해서 호출)
'''
# 단독 함수
help(len) # Help on built-in function len in module builtins:

# 메서드 
#help(split) # NameError: name 'split' is not defined
help(multiLine.split) # Help on built-in function split:
    # 단독함수가 아니고 객체에 의해 호출되므로 
    # 도움말을 볼 때도 아무 객체 먼저 써주고 그 후에 메서드 이름 써서 확인

# 문장 -> 단어 split
words = multiLine.split() # split(sep=' ')
words # ['This', 'is', 'multi', 'line', 'string']
len(words) # 5

# 최대 split 개수 지정 
multiLine.split(maxsplit=1)  ['This', 'is multi line\nstring']
# 생략된것: 구분자 sep = ' ' (디폴트)
# 즉 첫번째 ' '(공백)에서 스플릿 한번 

# 여러 개의 구분자로 split
string = '우리나라 대한,민국'
import re # 정규 표현식 함수 제공

# re.findall(pattern, string)
re.findall('[^,\s]+', string)
# 여기서 \s: 공백 
# ['우리나라', '대한', '민국']



# 2) join : 문자열 결합
# 단어 -> 문장 

# 형식) '구분자'.join(스트링객체)
sent = ' '.join(words)
sent #  'This is multi line string'

help(' '.join)
