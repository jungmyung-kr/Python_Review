"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-12 01:57:33 ~ 02:05:07
2022-07-13 02:05:08 ~
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

# 6-4 continue와 break

# 6-5 한줄 for

# 퀴즈 # 5

