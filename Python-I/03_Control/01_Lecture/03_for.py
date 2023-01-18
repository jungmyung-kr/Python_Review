"""
chap03_Control
step03_for
"""

'''
반복문(for)

형식) 
for  변수 in 반복가능객체 :
    실행문
    실행문

변수 in 반복 가능 객체 : 객체의 원소 순회 -> 변수 넘김
반복가능(iterable) 객체 : string 
'''


# 1. 문자열 객체
string = "나는 홍길동 입니다."
len(string) # 11
#  문자의 갯수 : 곧 반복의 횟수가 됨 

# 문자 -> 변수 넘김
for s in string : # 11회 반복 
    print(s, end = '') 
print()
# 나는 홍길동 입니다.

# 단어 -> 변수 넘김
for w in string.split(): # '나는' '홍길동' '입니다.' split으로 인해 공백 단위로 쪼개짐 : 3회 반복
    print(w)
'''
나는
홍길동
입니다.
'''    

# 2. list 객체 : 1차원 벡터 생성 
lst = [1, 2, 3, 4, 5]  # 1차원(vector)
for i in lst:
    print('원소 : ', i)
    

# 3. range 객체 : 순서 있는 정수 생성   
num1 = range(10)  
print('num1 : ', num1)  # range(0, 10) : object info

num2 = range(1, 10)
print('num2 : ', num2)  # range(1, 10)

for n in num1:
    print(n, end=' ')
print()
# 0 1 2 3 4 5 6 7 8 9

for n in num2:
    print(n, end=' ')
print()
# 1 2 3 4 5 6 7 8 9


# 4. list + range 객체 : 순서 있는 정수 -> 1차원 벡터 생성  

num2 = range(1, 5)  # 1~4
print('num2 : ', num2)  # num2 :  range(1, 5)

num2 = list(num2) # list형 변환 
print(num2)  # [1, 2, 3, 4]

lst = list(range(1, 101))  # 1 ~ 100
for i in lst:  # 100회
    if i % 5 == 0:
        print(i, end=' ')      
  
print()
# 5의 배수만 출력 : 
# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 


# 문) lst(1~100)에서 3의 배수이면서 5의 배수만 출력

lst = list(range(1,101))
for l in lst : 
    if l % 3 == 0 and l % 5 == 0 :
        print(l, end = ' ')

# 15 30 45 60 75 90 

# 5. 중첩 반복문

'''
for i in 열거형 객체 :
   for j in 열거형 객체 :
      실행문
'''

# 1) 구구단

for i in range(2,10) : # i변수 : 구구단의 단수
    # 바깥쪽 영역
    print('~~~ {}단 ~~~'.format(i))
    for j in range (1,10) : # j 변수: 곱수
        # 안쪽 영역
        print('%d * %d = %d' % (i, j, i * j))
'''
~~~ 2단 ~~~
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
...
~~~ 9단 ~~~
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
'''


# 2) 문자열 처리

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

print (string)

# 빈 벡터 선언
sents = [] # 문장 저장
words = [] # 단어 저장

# 문단 > 문장 > 단어
for s in string.split(sep='\n') : # 문단 -> 문장
    sents.append(s)
    for w in s.split(sep = ' ') : #문장 -> 단어
        words.append(w)
        
print('문장 : ', sents)
print('문장 갯수 : ', len(sents))
print('단어 : ', words)
print('단어 갯수 : ', len(words))

'''
문장 :  ['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 35세 입니다.']
문장 갯수 :  3
단어 :  ['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
단어 갯수 :  9
'''