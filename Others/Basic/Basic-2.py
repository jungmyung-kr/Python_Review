"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-07 00:00:00 ~ 00:13:12
2022-07-08 00:13:13 ~ 00:25:47
"""
# 2-1 숫자 자료형

print(5) # 양수
print(-10) # 음수
print(3.14) # 실수
print(5+3) # 덧셈
print(2*8) # 곱셈
print(3*(3+1)) # 혼합

# 2-2 문자열 자료형

print('ball') # 작은 따옴표
print("butterfly") # 큰 따옴표
print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*9) # 곱셈을 통해 위와 같은결과 출력 가능

# 2-3 boolean 자료형

# 참 / 거짓

print(5>10) # False
print(5<10) # True
print(True) # True
print(False) # False
print(not True) # False
print(not False) # True
print(not (5>10)) # = not False  = True

# 2-4 변수

# 값을 저장하는 공간 : 변수

# 변수 설정

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3


# 애완동물을 소개해 주세요~
print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) +"살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
# print(name , "는 어른일까요? " , is_adult)
# '+' 대신 ','도 사용 가능

'''
우리집 강아지의 이름은 연탄이예요
연탄이는 4살이며, 산책을 아주 좋아해요
연탄이는 어른일까요? True
'''

# 2-5 주석

# : 한문장 주석 처리

"""
이렇게 큰 따옴표나 
작은 따옴표로 
앞뒤를 둘러싸면 
여러 문장도 주석처리 가능
"""

# 또 다른 방법으로는 텍스트를 여러줄로 작성한 후,
# 전체 드래그하고 ‘ctrl + /‘를  눌러주면
# 한번에 주석 처리 가능

# 2-6 퀴즈 #1
'''
변수를 이용하여 다음 문장을 출력하시오.

변수명 
: station

변수값
: 사당, 신도림, 인천공항 (순서대로 입력)

출력문장
: XX 행 열차가 들어오고 있습니다.
'''

station = "사당" # "신도림", "인천공항"

print(station,"행 열차가 들어오고 있습니다.")
