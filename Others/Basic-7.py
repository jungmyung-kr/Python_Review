"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-13 02:28:36 ~ 02:37:49
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

# 7-4 키워드값

# 7-5 가변인자

# 7-6 지역변수와 전역변수

# 7-7 퀴즈 #6