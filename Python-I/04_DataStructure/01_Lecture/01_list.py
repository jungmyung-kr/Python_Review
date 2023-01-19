"""
chap04_DataStucture 
step01_list
"""

'''
list 특징
- 1차원 배열 구조(vector)
- 형식) 변수 = [값1,값2,...]
- 다양한 자료형 저장 : 숫자형, 문자형, 논리형 등에 상관없이 같은 객체에 다양하게 저장 가능
- 순서 존재(=색인을 사용할 수 있다.)
- 값 수정 가능 (추가, 삽입, 수정, 삭제)
    - 추가와 삽입의 차이: 추가는 맨 뒤에 추가 / 삽입는 중간에 삽입  
'''

# 1. 단일 list & 색인 

lst = list([1,2,3,4,5]) # class -> list 객체 
lst = [1,2,3,4,5] # 원래 문법은 위의 문장이나 list() 생략해 간소하게 써도 됨.
print(lst) # [1, 2, 3, 4, 5]
len(lst) # 5
print(type(lst)) # <class 'list'>
type(lst) # list : 위에꺼랑 출력 모양이 조금 다를뿐 결국은 같음


# 색인(index) : 값의 위치 (0부터 시작)
# 첫번째 : - start / 두번째 : - stop / 세번째 : step(인덱스간 간격)
lst[:] # 전체 원소. 원래 [1:4] 이런식으로 쓰는데 양변 숫자가 없으니 전체
lst # 이렇게 해도 전체 원소 나옴
lst[0] # 첫번째 원소. 
# 결과가 대괄호 없이 나옴 => 리스트 내의 원소라서 상수로 출력된 것
# 리스트 or 두개 이상의 원소 호출 시에는 [값,값...] 이렇게 출력 됨.
lst[2:4] # [3, 4]
lst[-1] # 마지막 원소 

# list + for 이용 

for i in lst : 
    print(i, end = ' ') # 한 줄로 나란히 출력 
    print(lst[i-1]) # 색인을 수식으로 적용한 사례 ex) i =1 -> i-1=0 -> lst[0]
'''
1 1
2 2
3 3
4 4
5 5
'''

# range(start, stop, step)

x=list(range(1,101)) # range : 1~100까지 숫자 생성, list로 그걸 리스트로 만들어줌
type(x) #list
print(x)

# 객체[start:stop-1]

print(x[:5]) # 앞 부분 5개 원소 확인 : [1, 2, 3, 4, 5]
print(x[-5:]) # 뒷 부분 5개 원소 확인 : [96, 97, 98, 99, 100]

# 객체[start:stop:step]

print(x[::2]) # 홀수 수열
print(x[1::2]) # 짝수 수열


# 2. 중첩 list & 색인 

y = [['a','b','c'], [1,2,3]] 
print(y) # [['a', 'b', 'c'], [1, 2, 3]]
len(y) # 2 : 즉 각 리스트 내의 원소수를 세는 것이 아니라 y내 리스트 수가 출력 됨.

print(y[0]) # ['a', 'b', 'c']
print(y[1]) # [1, 2, 3]

print(y[0][2]) # y내 0번째 리스트 선택 [0] -> 0번째 리스트 내 2번째 원소 선택 [2] => c
print(y[1][1]) # y내 1번째 리스트 선택 [1] -> 1번째 리스트 내 2번째 원소 선택 [1] => 2
print(y[1][1:]) # y내 1번째 리스트 선택 [1] -> 1번째 리스트 내 1번째~끝까지 원소 선택 [1:] => [2, 3]


# 3. 값 수정(추가, 삽입, 수정, 삭제)

num = ['one', 2, 'three', 4] # 다양한 자료형 가능 
# R의 경우 하나라도 문자형이면 전체 데이터형이 문자로 바뀌는데 python은 아님. 그냥 원래 형태대로 다 담음.
print(num) # ['one', 2, 'three', 4]

# 1) list 추가 
num.append('five') 
print(num) # ['one', 2, 'three', 4, 'five']
len(num) # 5

# 2) list 삭제 
num.remove('three')
print(num) # ['one', 2, 4, 'five']

# 3) list 수정 : 색인 이용 
num[1] = 'two' 
print(num) # ['one', 'two', 4, 'five']

# 4) list 삽입 
num.insert(0, 'zero') # (index, object) : 0번째 위치에 'zero' 삽입
print(num) # ['zero', 'one', 'two', 4, 'five']


# 4. list 연산 

x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+)
z = x + y # 내부 원소끼리 더하기한 값을 구해주는 것이 아니라 말그대로 리스트 두개 합쳐 새로운 객체에 결합
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장 
x.extend(y) #  # 단일 list (o) : x에 y를 끼워넣음 (위에 결합은 새로운 객체에 두 리스트 원소를 넣는 것)
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가 
# 변수명.append('추가할 원소')
x.append(y) # 단일 list (x) 중첩 list (o)
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]
len(x) # 7

# 4) list 반복(*)
result = y * 2 # -> 리스트를 반복하는 것. 
print(result) # [1.5, 2.5, 1.5, 2.5]

# y의 원소에 2를 곱하는 의미가 아님(이건 바로 및 for문 참조.) 
# result = y * 0.5 이런 것도 당연히 불가. 
# 산술 연산은 for문 사용해서 작성해야 함.


# 각 원소에 산술 연산: for문 사용
for el in y : # [1.5, 2.5]
    print(el * 2)

'''
3.0
5.0
'''    
    

# 5. list에서 원소 찾기 

'''
if '원소' in list :
    list에 '원소' 포함 
'''

num = [] # 빈 list : 숫자 저장 

# 임의 숫자 입력 
for i in range(5) : # 0~4
    num.append(int(input()))
    
# 임의의 숫자를 5개 입력 받아서 num에 저장하게 하는 구조 

print(num) # [1, 2, 3, 4, 5] : 내가 임의로 입력한 숫자 5개 출력


# 숫자 원소 찾기 
if int(input()) in num :
    print('숫자 있음')
else :
    print('숫자 없음')

# 6. list 객체 method
# method : 해당 객체의 자료를 조작하는 함수
# 형식) 객체.메서드()

import random # 난수 생성 함수 모듈 
r = [] # 빈 list : 난수 저장용

# 난수 10개 생성
for i in range(10) :
    r.append(random.randint(1,10)) # 1~10 난수 정수

print(r) # [7, 3, 10, 10, 2, 7, 3, 1, 10, 5]
len(r) # 10
type(r) # list 

# 메서드 확인
dir(r)
'''
'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
 '''
 
r.count(10) # 3 : 전체 원소 중에 ()안의 값이 몇 번 나왔는지 객체 수 반환
r.count(4) # 0 (해당 객체 없음)

r.pop(0) # index에 값을 반환,제거 : 0번째 객체 제거
print(r) # [3, 10, 10, 2, 7, 3, 1, 10, 5]
len(r) # 9
r.index(10) # object의 색인 반환
r.index(4) # 해당 값 없는 경우 ValueError: 4 is not in list

# 정렬
r.sort() # 오름차순 
r # [1, 2, 3, 3, 5, 7, 10, 10, 10]

r.sort(reverse =True) # 내림차순
r #  [10, 10, 10, 7, 5, 3, 3, 2, 1]
r.reverse() # 현재 값의 역순 

# 복제(copy)
r2 = r.copy() # 깊은 복사
print(r2) # [10, 10, 10, 7, 5, 3, 3, 2, 1]
id(r) # 2868856363456
id(r2) # 2868856362048 : 내용은 r과 같으나 주소가 다름

r3 =r # 얕은 복사 (주소 복사)
print(r3) # [10, 10, 10, 7, 5, 3, 3, 2, 1]
id(r3) # 2868856363456 : 내용, 주소 모두 r과 일치

# 원소와 객체 제거
r.remove(10) # 특정 원소 제거 
print(r) # [10, 10, 7, 5, 3, 3, 2, 1]

r.clear() # 전체 원소 제거
print(r) # []

# 메모리에 저장된 객체 자체를 제거 (Variable Explorer에 뜨는 객체들)

del r 
# 이건 메서드가 아니라 파이썬 자체 명령어라서 "객체.메서드" 구조가 아님

print(r) 
# NameError: name 'r' is not defined
# 객체가 제거되었기 때문에 출력 불가