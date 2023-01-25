"""
chap06_Function
step01_user_func
"""


'''
1. 함수(function)
- 중복 코드 제거 
- 재사용
- 기능 정의

2. 사용자정의함수  
형식)
def 함수명(인수) :
    실행문
    실행문
    return 값
'''

# 1. 인수가 없는 함수 
def userFunc1() :
    print('userFunc1')
    print('인수가 없는 함수')


# 2. 인수가 있는 함수 
def userFunc2(x, y) :
    z = x + y
    print('z =', z)

# 3. return 있는 함수 
def userFunc3(x, y) :
    add = x + y
    sub = x - y     
    mul = x * y
    div = x / y
    return add, sub, mul, div # 여러개 값 반환 

# 함수를 호출하는 방법

userFunc1() 
# 인수가 없는 함수 호출

userFunc2(10,20)
# 인수가 있는 함수이므로 인수를 기입해주고 실행해야 함.
# z = 30

userFunc3(10, 2)
# 인수가 있는 함수이므로 이 또한 기입해주고 함수 호출해야함. 
# R과 달리 한번에 여러값 반환
# (12, 8, 20, 5.0)

a,s,m,d = userFunc3(10, 2)
# 이건 위의 값을 각각 변수에 저장하는 것 
# 생성되는 값이 나열된 변수 순으로 저장됨.
print(a) # 12


# 1차 방정식 예
def fx(x) : # x 변수
    y = 2*x + 3 # x^1 즉 1차 방정식= ax+b / 그래프 직선
    return y

fx(1) #5
fx(2) #7
fx(3) #9

import matplotlib.pyplot as plt # as 별칭

x = list(range(1,11)) # 1~10
x # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list 내포
y = [fx(i) for i in x]
print (y) # [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

plt.plot(x, y) # 선 그래프
plt.show() # 그래프 보이기


# 2차 방정식 예
def fx(x) : # x 변수
    z = 2*x**2 + 3*x + 2 # x^2 즉 2차 방정식 = ax^2 + bx + c / 그래프 곡선
    return z

fx(1) #7
fx(2) #16
fx(3) #29

import matplotlib.pyplot as plt # as 별칭

x = list(range(1,11)) # 1~10
x # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list 내포
z = [fx(i) for i in x]
print (z) # [7, 16, 29, 46, 67, 92, 121, 154, 191, 232]

plt.plot(x, z) # 선 그래프
plt.show() # 그래프 보이기