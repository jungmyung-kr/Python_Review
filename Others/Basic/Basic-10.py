"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-22 04:50:13 ~05:14:22
"""

# 10-1 예외 처리

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요. : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요. : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

'''
1) 정상
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요. : >? 6
두 번째 숫자를 입력하세요. : >? 3
6 / 3 = 2

2) 정수 대신 문자열 입력 
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요. : >? 6
두 번째 숫자를 입력하세요. : >? 삼
에러! 잘못된 값을 입력하였습니다.

3) 0으로 나누기
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요. : >? 6
두 번째 숫자를 입력하세요. : >? 0
division by zero

4) 코드 중 일부 주석 처리해 일부러 오류 발생시킴
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요. : >? 6
두 번째 숫자를 입력하세요. : >? 3
알 수 없는 에러가 발생하였습니다.
list index out of range
'''

# 10-2 에러 발생 시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

'''
1) 정상
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 6
두 번째 숫자를 입력하세요 : >? 3
6 / 3 = 2

2) 두 자리 숫자 입력
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 10
두 번째 숫자를 입력하세요 : >? 5
잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
'''


# 10-3 사용자 정의 예외 처리


class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 10
두 번째 숫자를 입력하세요 : >? 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
'''

# 10-4 finally

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

'''
에러 발생 여부와 상관없이 무조건 실행됨 

1) 정상
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 6
두 번째 숫자를 입력하세요 : >? 3
6 / 3 = 2
계산기를 이용해 주셔서 감사합니다.

2) 에러1 
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 6
두 번째 숫자를 입력하세요 : >? 삼
잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
계산기를 이용해 주셔서 감사합니다.

2) 에러2
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : >? 10
두 번째 숫자를 입력하세요 : >? 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
계산기를 이용해 주셔서 감사합니다.
'''

# 10-5 퀴즈 # 9

'''
Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있스니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
          출력 메세지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문 할 수 있는 총 치킨의 양은 10마리로 한정
           치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
           출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."          
'''


class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1  # 홀 안에는 현재 만석. 대기번호 1부터 시작
while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." \
                  .format(waiting, order))
            waiting += 1
            chicken -= order

            if chicken == 0:
                raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

'''
1) 정상 주문 : 5마리
[남은 치킨 : 10]
치킨 몇 마리 주문하시겠습니까?>? 5
[대기번호 1] 5마리 주문이 완료되었습니다.

2) 정상 주문 : 3마리
[남은 치킨 : 5]
치킨 몇 마리 주문하시겠습니까?>? 3
[대기번호 2] 3마리 주문이 완료되었습니다.

3) 오류 : 0마리 주문
[남은 치킨 : 2]
치킨 몇 마리 주문하시겠습니까?>? 0
잘못된 값을 입력하였습니다.

4) 오류 : -1마리 주문
[남은 치킨 : 2]
치킨 몇 마리 주문하시겠습니까?>? -1
잘못된 값을 입력하였습니다.

5) 오류: 문자 입력
[남은 치킨 : 2]
치킨 몇 마리 주문하시겠습니까?>? 2마리
잘못된 값을 입력하였습니다.

6) 정상 주문 : 2마리, 재고 소진 완료
[남은 치킨 : 2]
치킨 몇 마리 주문하시겠습니까?>? 2
[대기번호 3] 2마리 주문이 완료되었습니다.
재고가 소진되어 더 이상 주문을 받지 않습니다.
'''