"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-12 01:57:33 ~ 02:28:35
"""

# 6-1 if
'''
if 조건 : 
    실행 명령문
'''
# 예시 1
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")

# 예시 2
temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

# 6-2 for

# 예시 1
for wating_no in range(1, 6):
    print("대기번호 : {0}".format(wating_no))
'''
대기번호 : 1
대기번호 : 2
대기번호 : 3
대기번호 : 4
대기번호 : 5
'''

# 예시 2
starbucks = ["Ironman", "Thor", "Groot", "Spiderman"]
for customer in starbucks:
    print("{0}고객님, 커피가 준비되었습니다.".format(customer))

# 6-3 while

# 예시 1
customer = "Thor"
index = 5
while index >= 1:
    print("{0}손님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분되었습니다.")

# 예시 2 : 무한 루프
customer2 = 'Ironman'
index = 1
while True:
    print("{0}손님, 커피가 준비되었습니다. 호출{1}회".format(customer2, index))
    index += 1

# 예시 3
customer3 = "Groot"
person = "Unknown"
while person != customer3:
    print("{0}손님, 커피가 준비되었습니다.".format(customer3))
    person = input("이름이 어떻게 되세요?")

# 6-4 continue와 break
# 출석한 학생들에게 책 읽게 함
# 결석한 학생 넘어감
# 책 안가져온 학생 있으면 수업 바로 종료

absent = [2, 5]  # 결석한 출석 번호
no_book = [7]  # 책을 안 가져온 학생
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업은 여기까지. {0}번은 교무실로 오세요.'.format(no_book))
        break
    print('{0}번, 책을 소리내어 읽어보세요.'.format(student))

'''
1번, 책을 소리내어 읽어보세요.
3번, 책을 소리내어 읽어보세요.
4번, 책을 소리내어 읽어보세요.
6번, 책을 소리내어 읽어보세요.
오늘 수업은 여기까지. [7]번은 교무실로 오세요.
'''

# 6-5 한줄 for

# 예시 1
# 출석번호가 1 2 3 .... 였는데 작성방식 변경
# 앞에 100을 붙이기로 함 -> 101, 102, 103, ...

students = [1, 2, 3, 4, 5]
print(students)  # [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)  # [101, 102, 103, 104, 105]

# 예시 2
# 학생 이름을 길이로 변환
students2 = ['Groot', 'Ironman', 'Spiderman', 'Thor']
print(students2)  # ['Groot', 'Ironman', 'Spiderman', 'Thor']
students2 = [len(i) for i in students2]
print(students2)  # [5, 7, 9, 4]

# 예시 3
# 학생 이름을 대문자로 변경
students3 = ['steve', 'nancy', 'robin', 'jonathan']
print(students3)  # ['steve', 'nancy', 'robin', 'jonathan']
students3 = [i.upper() for i in students3]
print(students3)  # ['STEVE', 'NANCY', 'ROBIN', 'JONATHAN']

# 퀴즈 # 5
'''
Quiz) 당신은  uber 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. 

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[  ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[  ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''
from random import *

index = 0
total_customer = 0  # 총 탑승 승객 수

for index in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(index, time))
        total_customer += 1
    else:
        print('[  ] {0}번째 손님 (소요시간 : {1}분)'.format(index, time))
    index += 1
print('총 탑승 승객 : {0}분'.format(total_customer))
'''
[  ] 1번째 손님 (소요시간 : 18분)
[  ] 2번째 손님 (소요시간 : 35분)
[  ] 3번째 손님 (소요시간 : 28분)
...
[O] 48번째 손님 (소요시간 : 7분)
[  ] 49번째 손님 (소요시간 : 19분)
[  ] 50번째 손님 (소요시간 : 27분)
총 탑승 승객 : 15분
'''
