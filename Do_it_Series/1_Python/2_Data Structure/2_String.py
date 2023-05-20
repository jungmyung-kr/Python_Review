# String 

"a"
'Python is fun'

"""Life is too short, you need Python"""
'''Life is too short, you need Python'''

# 큰 따옴표 안에 작은 따옴표 포함

food = "Python's favorite food is perl"
food # "Python's favorite food is perl"

food = 'Python's favorite food is perl'
# SyntaxError: invalid syntax

# 문자열에 큰 따옴표 포함

say = "Python is very easy." he says."
# SyntaxError: invalid syntax

say = "\"Python is very easy. \" he says."
say # '"Python is very easy. " he says.'

# 여러 줄 

multiline = """
Life is too short.
You need Python
"""
multiline

# 문자열 연산

head = "Python"
tail = " is fun!"
head + tail # 'Python is fun!'

a = "python"
a * 2 # 'pythonpython'

print('='*50)
print('My Program')
print('='*50)

# 문자열 길이 구하기 

a = "Life is too short"
len(a) # 17

b = "You need python"
len(b) # 15

# 문자열 인덱싱과 슬라이싱 

a = "Life is too short, You need Python"
a[3] # 'e'
a[0] # 'L'
a[12] # 's'
a[-1] # 'n'
a[-2] # 'o'

b = a[0] + a[1] + a[2] + a[3]
b # 'Life'

b = a[0:4]
b # 'Life'

a[0:2] # 'Li'
a[5:7] # 'is'
a[12:17] # 'short'

a[19:] # 'You need Python'
a[:17] # 'Life is too short'
a[:] # 'Life is too short, You need Python'

a[19:-7] # 'You need'

# 슬라이싱으로 문자열 나누기

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date # '20010331'
weather # 'Rainy'

year = date[:4]
month = date[4:6]
day = date[6:8]

year # '2001'
month # '03'
day # '31'

a = 'pithon'
a = a[0] + 'y' + a[2:]
a # 'python'

# 문자열 포맷팅

"I eat %d apples." %3 # 'I eat 3 apples.'
"I eat %s apples" %'five' # 'I eat five apples'

number = 3
'I eat %d apples.' %number # 'I eat 3 apples.'

number = 10 
day = "Three"
"I ate %d apples. So I was sick for %s days." %(number, day)
# 'I ate 10 apples. So I was sick for Three days.'

"I have %s apples" % 3 # 'I have 3 apples'
"rate is %s" % 3.234 # 'rate is 3.234'

"Error is %d%%" % 98 # 'Error is 98%'

# 포맷 코드와 숫자 함께 사용하기 

    # 정렬과 공백

"%10s" % "hi" # '        hi'
"%-10s jane" % "hi" # 'hi         jane'

    # 소수점 표현하기
"%0.4f" % 3.42134234 # '3.4213'
"%10.4f" % 3.42134234 # '    3.4213'

# format 함수를 사용한 포맷팅 

"I eat {0} apples.".format(3) # 'I eat 3 apples.'

"I eat {0} apples.".format("five") # 'I eat five apples.'

number = 3
"I eat {0} apples.".format(number) # 'I eat 3 apples.'

number = 10 
day = "three"
"I ate {0} apples. So I was sick for {1} days.".format(number, day) 
# 'I ate 3 apples. So I was sick for Three days.'

"I ate {number} apples. So I was sick for {day} days.".format(number=9, day='two')
# 'I ate 9 apples. So I was sick for two days.'

"I ate {0} apples. So I was sick for {day} days.".format(10, day ='three')
# 'I ate 10 apples. So I was sick for three days.'

    # 왼쪽 정렬
"{0:<10}".format("hi") # 'hi        '

    # 오른쪽 정렬
"{0:>10}".format("hi") # '        hi'

    # 가운데 정렬
"{0:^10}".format("hi") # '    hi    '

    # 공백 채우기
"{0:=^10}".format("hi") # '====hi===='
"{0:!^10}".format("hi") # '!!!!hi!!!!'

    # 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) # '3.4213'
"{0:10.4f}".format(y) # '    3.4213'

    # { 또는 } 문자 표현하기
"{{ and }}".format() # "{ and }"


# f 문자열 포맷팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}살입니다.' 
# '나의 이름은 홍길동입니다. 나이는 30살입니다.'

age = 30 
f'나는 내년이면 {age+1}살이 된다.'
# '나는 내년이면 31살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# '나의 이름은 홍길동입니다. 나이는 30입니다.'

# 문자열 관련 함수

    # 문자 개수 세기 

a = "hobby"
a.count('b') # 2

    # 위치 알려주기 
a = "Python is the best choice"
a.find('b') # 14
a.find('k') # -1

    # 위치 알려주기 2
a = "Life is too short"
a.index('t') # 8
a.index('k') # ValueError: substring not found

    # 문자열 삽입 
",".join('abcd') # 'a,b,c,d'

    # 소문자를 대문자로 바꾸기 
a = "hi"
a.upper() #'HI'

    # 대문자를 소문자로 바꾸기
a = "BYE"
a.lower() # 'bye'

    # 왼쪽 공백 지우기 
a = " hi "
a.lstrip() # 'hi '

    # 오른쪽 공백 지우기
a = " hi "
a.rstrip() # ' hi'

    # 양쪽 공백 지우기 
a= " hi "
a.strip() # 'hi'


    # 문자열 바꾸기 
a = "Life is too short"
a.replace("Life", "Your leg") # 'Your leg is too short'

    # 문자열 나누기 
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(":") # ['a', 'b', 'c', 'd']