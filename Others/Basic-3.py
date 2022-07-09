
"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-09 00:25:48 ~
"""

# 3-1 연산자

print(1 + 1) # 2 
print(3 - 2) # 1
print(5 * 2) # 10 
print(6 / 3) # 2 

print(2 ** 3) # 2^3=8
print(5 % 3) # 나머지 구하기 2
print(10 % 3) # 1
print(5 // 3) # 몫 1 
print(10 // 3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False

print(1 != 3) # True
print(not (1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 3-2 간단한 수
 
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = (2 + 3 * 4)
print(number)

number = number + 2 # 16
print(number)

number += 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 5 # 1
print(number)

# 3-3  숫자처리함수

print(abs(-5)) # 절댓값 : 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 최댓값 : 12
print(min(5, 12)) # 최솟값 : 5
print(round(3.14)) # 반올림 : 3
print(round(4.99)) # 5


from math import * 
print(floor(4.99)) # 버림 : 4
print(ceil(3.14)) # 올림 : 4
print(sqrt(16)) # 제곱근 : 4

# 3-4 랜덤함수
# 3-5 퀴즈 #2