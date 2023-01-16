'''
step03_print_input.py

1.print(): 표준 출력 장치 - 콘솔 출력
2.input(): 표준 입력 장치 - 키보드 입력
'''


# 1. print() 
# - 콘솔 출력 함수 

help(print) # 함수 도움말
# Help on built-in function print in module builtins:
    # 즉 print는 builtin module에 포함된 함수라는 의미 = 내장 함수
    # 임포트 하지 않고 바로 사용이 가능핟. 
#  print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#  value: 콘솔에 출력할 값 
#  sep: 각 원소들 구분할 때 구분자 ' '라면 공백 한칸
#  end='\n' : 프린트 문이 있을 때 마다 줄 바꿔줌 (디폴트)
#  file=sys.stdout : 파일을 출력할 때 콘솔창에 출력할 것인지 
                   # 별도의 출력장치(ex.프린터)로 출력할 것인지
#  file과 flush는 잘 안씀. 

# 1) 기본 인수 
print("value =",10,10+20)  # value = 10 30 (디폴트 sep= ' ')
print('010','1234','1111', sep='-') # 010-1234-1111

# end 속성 
print('value =', 10, end=',') 
print('value =', 20) 
# end = '\n'가 디폴트, 저렇게 바꿔주면
# value = 10,value = 20 
# 이렇게 두개의 print값이 ,로 구분되면서 한줄로 나열

# 2) % 양식문자 
# 형식) print('%양식문자' %값)

num1 = 10; num2 = 20
tot = num1 + num2 
print('%d + %d = %d' %(num1, num2, tot)) 
# 10 + 20 = 30

print('이름은 %s이고, 나이는 %d 이다.' %('홍길동', 35))
# 이름은 홍길동이고, 나이는 35 이다.
print('원주율 = %8.3f' %(3.14159)) 
# 전체 자릿 수 8자리로 하되, 소수점 이하 자리는 3자리까지 (나머지는 정수 자리로)
# 원주율 =    3.142
print('원주율 = %.3f' %(3.14159))
# 정수 자리는 무한으로 하되, 소수점 이하 자리는 3자리까지
# 원주율 = 3.142

# 50%
print('전체 찬성률은 %d%%이다.'%(50)) 
# 전체 찬성률은 50%이다.


# 3) format()함수 이용 

# 형식1) print('{형식}'.format(값))
print('이름은 {}이고, 나이는 {}이다.'.format('홍길동', 35))
# {}안에 별 다른 값을 지정하지 않고 format에 값 써주면 그 순서대로 들어감
# 이름은 홍길동이고, 나이는 35이다.

#'{위치:형식}'
print('정수형 = {0}, {1:5d}, 연봉 : {2:3,d}'.format(123, 1234, 2500))
# {0},{1},{2} : 0번째, 1번째, 2번째 원소를 넣어라 (파이썬은 일반적으로 1번째인것이 0번째라고 표현함)
# : 뒷부분: d=digit 10진수, d앞숫자: 자릿수  
# ex) {1:5d} 1번째 원소, 5자리수를 갖는 십진수(d)의 포맷으로 출력해라
# ex) {2:3,d} 2번째 원소, 10진수, 천단위마다 , 찍어 출력하라
# 정수형 = 123,  1234, 연봉 : 2,500


print('원주율 = {0:.3f}, {1:8.3f}'.format(3.14159, 3.14159))
# 원주율 = 3.142,    3.142
# 뒤에 원소 출력될 때 띄어쓰기 많이 된 이유 
# 앞에 원소 : 정수 자리수 지정 없이 소수점 이하 자리수만 3자리 확보, 공백 필요 없음
# 뒤에 원소 : 전체 자리수 8개 확보 후 소수점 이하 3자리 써버림 = 정수자리 5개 확보됨
#            3.142를 보면 정수자리 1개만 값이 있으므로 나머지 4개가 공백으로 나옴  


# 형식2) format(값, '양식')
print('원주율 = ', format(3.14159, '5.3f')) # 원주율 =  3.142
# 이렇게 값 쓰고 바로 뒤에 양식을 써주는 것도 가능
# '{}' <- 이렇게 안해도 된다는 것

print('금액=', format(5421000,'3,d')) # 금액= 5,421,000

# 축약형 format: SQL 문
name = '홍길동'; age = 35
sql = f"select from emp where name = '{name}' and age ={age}"
print(sql)
# select from emp where name = '홍길동' and age =35

# 2. input()
# - 키보드로 입력받는 함수 

# 키보드 입력 -> 정수형 변환 
a = int(input('첫번째 숫자 입력 : ')) # 10
b = int(input('두번째 숫자 입력 : ')) # 20
# int로 감싸지 않으면 기본적으로 input은 문자로 인식함 
# 그래서 print(c)하면 1020 이렇게 나열됨. 
# int로 감싸줘서 정수형으로 변환해줘야 연산이 가능함.

c = a + b
print('c=', c) # c= 30

# 키보드(문자) -> 실수형 변환  
x = float(input('첫번째 실수 입력 : ')) # ex) 12.5
y = float(input('두번째 실수 입력 : ')) # ex) 32.6
z = x + y
print('z=', z) # ex) z =45.1


# 3. 자료형 변환(casting)
print(int(24.564)) 
# 24 : 실수 -> 정수 변환

print(2 + '2') 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 연산에 오류 발생, 뒤에는 문자열이기 때문

print(2 +int('2')) # 4
# 이건 가능! 숫자 + 문자 -> 숫자 + 정수로 변환

int('hello') 
# ValueError : invalid literal for int() with base 10: 'hello'
# 위의 '2'는 따옴표만 떼면 숫자이기 때문에 문자여도 숫자로 변환 가능
# 하지만 hello는 본질이 문자이므로 불가 

print('나이 :' + str(35)) # 나이 :35 : 문자 + 문자(정수) -> 문자열 변환

# 논리형(boolean) -> 정수형 변환
int(True) # 1
int(False) # 0

# 숫자형 -> 논리형 변환
bool(12.5664) # True : 0이 아닌 모든 수
bool(0) # False : 0