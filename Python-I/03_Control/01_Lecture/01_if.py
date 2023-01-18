"""
chap03_Control
step01_if
"""

'''
제3장 제어문 : 조건문 + 반복문
1. 조건문(if)
 블록: 콜론과 들여쓰기(tab키)
 내어쓰기 : shift + tab
'''

'''
형식1)
if 조건식 :
    실행문
'''

var = 10 # 초기화 
if var >= 5 :
    print('var =', var)
    print('var는 5보다 크다.') # 들여쓰기 : 조건에 충족해야 출력된다.

print('항상 실행 영역') # 내어쓰기 : 조건과 무관하다.

'''
형식2) if~else 
if 조건식 :
    실행문1 : True
else :
    실행문2 : False 
'''

var = int(input('var 변수에 값 입력 : ')) # 키보드 입력 

if var >= 5 :
    print('var는 5 이상')
else :
    print('var는 5 미만')


if var % 5 == 0 :
    print ('var는 5의 배수')    
else :
    print('var는 5의 배수가 아님')


'''
형식3) 연속적 if~else 
if 조건식1 :
    실행문1 -> 조건식1 True
elif 조건식2 :
    실행문2 -> 조건식2 True
else :
    실행문3 -> 모든 조건 False
'''


# 점수 : 100~85 : '우수', 84~70 : '보통', 70 미만 : '저조'

score = int(input('점수 입력: ')) # 점수 

# 중첩 if ~ else 
if score < 0 or score > 100 :
      print('점수 잘못 입력')
      grade = '오류'
else :
    if score >= 85 :
        print('우수')
        grade = '우수'
    elif score >= 70 :
        print('보통')
        grade = '보통'
    else :
        print('저조')
        grade = '저조'
print('점수는 %d점이고, 등급은 \'%s\'이다.'%(score,grade))


# 블록 if vs 한 줄 if 

# 1) 블록 if
num = 9

if num >= 5 :
    result = num + 5
else : 
    result = num * 5 

print('result = ', result) # result = 14


# 2) 한줄 if 
# 형식) 변수 = if 조건식 else 거짓
result = num + 5 if num >= 5 else num * 5
print('result = ',result) # result = 14


# 원소 찾는 경우
# if 조건식 in dataset : 

names = ['홍길동','이순신','유관순']
print(names) 

if '이순신' in names : 
    print ('찾는 이름 있음') # 찾는 이름 있음
else :
    print ('찾는 이름 없음')