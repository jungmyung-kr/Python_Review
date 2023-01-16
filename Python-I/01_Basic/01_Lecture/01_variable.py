"""
chap01_Basic
step01. Variable
"""

"""
변수(Variable)
 - 자료가 저장된 메모리 이름
 - 형식) 변수명 = 값(수식, 변수명)
"""

# 1. 변수와 자료형 
var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)

# type : 객체 출처 확인 (자료형 확인) 
print(type(var1), type(var2)) 
# <class 'str'> <class 'str'>
# str : string 문자형

var1 = 100 # 변수 수정  
print(var1, type(var1)) 
# 100 <class 'int'>
# 변수는 R과 마찬가지로 최근에 입력된 값이 남음

var3 = 123.2345
print(var3, type(var3)) 
# 123.2345 <class 'float'>

var4 = True #True, False
print(var4, type(var4)) 
# True <class 'bool'> 
# bool : 논리형



# 2. 변수명 작성 규칙
'''
- 첫자 : 영문자 or _ 사용가능 
- 두번째 : 숫자 사용 가능 
- 대소문자 구분(Score, score)
- 낙타체 : 두 단어 결합(korScore) (두단어 결합시 두번째 단어 첫글자 - 대문자)
- 키워드(클래스명, 함수명) 사용불가, 한글명 비권장
- 점(.) 사용 불가  
'''

_num10 = 10
_Num10 = 20

print(_num10 * 2) # 20
print(_Num10 * 2) # 40
# 대소문자 구분하는 것을 확인할 수 있음


# 낙타체
korScore = 89
matScore = 75
engScore = 55

tot = korScore + matScore + engScore
print('총점 =', tot) # 총점 = 219

# member.id = 'hong'
# 이렇게 '.' 포함해서 변수명 저장 불가. 특문: 언더바'_'만 가능
member_id = 'hong'
print(member_id)

# 키워드 사용 불가
# True = 10
# True는 논리형의 상수로 이미 사용하고 있으므로 변수명 설정 불가

# Python 키워드 확인
import keyword # module import 
'''
모듈명.멤버
ex) keyword.kwlist
모듈은 R의 package와 비슷한 개념임
'''
kword = keyword.kwlist # 키워드 제공
print(kword)
"""
['False', 'None', 'True', 'and', 'as', 'assert',
 'async', 'await', 'break', 'class', 'continue', 
 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in',
 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
 'raise', 'return', 'try', 'while', 'with', 'yield']
즉 이런 키워드들은 변수명으로 설정할 수 없다.
"""
print('명령어 갯수 : ', len(kword)) # 명령어 갯수 :  35



# 3. 참조변수 : 객체가 저장된 메모리 주소 저장
x = 150 # x는 150 객체의 주소 저장 
x2 = x # x의 주소 복사 
# x, x2 모두 같은 주소를 가지고 있다.
# 밑에 id() 부분 추가 설명

print(x) # x주소 접근 -> 150 출력 
print(x2) # 150

#id() : 해당 변수의 주소 출력
# 변수의 주소 출력
print(id(x)) # 140727080663504
print(id(x2)) # 140727080663504
# 주소가 같다. 같은 객체를 참조. 내용 동일

# 객체가 동일하면 주소도 동일함
y = 45.23
y2 = 45.23

print(id(y),y) # 1988093859184 45.23
print(id(y2), y2) # 1988093858896 45.23