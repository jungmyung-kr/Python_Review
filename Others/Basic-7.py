"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-13 02:28:36 ~ 02:37:49
2022-07-14 02:37:50 ~ 02:58:58
"""

# 7-1 함수


def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


# 7-2 전달값과 반환값
# 예제 1 : 입금

def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money


balance = 0
balance = deposit(balance, 1000)
print(balance)

# 예제 2 : 출금


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금하려는 금액과 같거나 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 불가합니다. 잔액은 {0}원입니다.".format(balance))
        return balance


balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 1000)
print(balance)
'''
입금이 완료되었습니다. 잔액은 2000원입니다.
출금이 완료되었습니다. 잔액은 1000원입니다.
1000
'''
balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 3000)
print(balance)
'''
입금이 완료되었습니다. 잔액은 2000원입니다.
출금이 불가합니다. 잔액은 2000원입니다.
2000
'''

# 예제 3 : 야간 출금, 수수료


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commission, balance))
'''
입금이 완료되었습니다. 잔액은 1000원입니다.
수수료는 100원이며, 잔액은 400원입니다.
'''

# 7-3 기본값


def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
          .format(name, age, main_lang))


profile("Edwin", 20, "Python")
profile("Jose", 25, "Java")
'''
이름 : Edwin	나이 : 20	주 사용 언어 : Python
이름 : Jose	나이 : 25	주 사용 언어 : Java
'''

# 같은 학교 같은 학년 같은 반 같은 수업


def profile(name, age=17, main_lang="Python"):  # 기본 값 설정
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
          .format(name, age, main_lang))


profile("Edwin")
profile("Jose")
'''
기본값으로 나이와 주 사용 언어를 설정해두었기 때문에,
이름만 기입하면 기본값을 그대로 출력해주는 것을 확인 할 수 있음

출력 결과 : 
이름 : Edwin	나이 : 17	주 사용 언어 : Python
이름 : Jose	나이 : 17	주 사용 언어 : Python
'''

# 7-4 키워드값


def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="Edwin", main_lang="Python", age=20)
profile(main_lang="Java", age=25, name="Jose")
'''
순서를 다르게 입력해도, 키워드에 맞춰 값을 기입함으로써
함수에 정의한 순서대로 값을 반환해 주는 것을 확인 할 수 있음.

출력 결과 : 
Edwin 20 Python
Jose 25 Java
'''

# 7-5 가변인자


def proflie(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


# 개인별로 익힌 언어의 갯수가 다를 수 있으므로,
# def proflie(name, age, lang1, lang2, lang3 ... 이렇게 일일이 기입하는 것 보다
# *language로 지정하고 for문을 사용하는 것이 합리적

proflie("Louis", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# 이름 : Louis	나이: 20	 Python Java C C++ C# JavaScript

proflie("Lisbeth", 25, "Kotlin", "Swift")
# 이름 : Lisbeth	나이: 25	 Kotlin Swift

# 7-6 지역변수와 전역변수

gun = 10


# 방법 1
def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용 : 함수 내에서가 아니라 전체에 사용 가능
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
'''
전체 총 : 10
남은 총 : 8
'''


# 방법 2 : 방법 1처럼 전역변수를 쓸 수도 있지만
# 나중에 코드 관리가 힘들기 때문에 이렇게 하는 것이 낫다고 함.
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
'''
전체 총 : 10
남은 총 : 8
'''

# 7-7 퀴즈 #6

'''
Quiz)  표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21 

조건 1 : 표준 체중은 별도의 함수 내에서 계산
             * 함수명 : std_weight
             * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제) 
키 175cm 남자의 표준 체중은 67.38kg입니다. 
'''


def std_weight(height, gender):

    if gender == "남자":
        return height * height * 22
    else:
         return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다. ".format(height, gender, weight))