"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-15 02:58:59 ~ 03:10:11
"""

# 8-1 표준입출력

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
'''
수학 0
영어 50
코딩 100

수학      :      0
영어      :    50
코딩      :  100
'''

# 은행 대기 순번표
# 001, 002, 003, ....

for num in range(1, 21):
    print("대기번호 :" + str(num).zfill(3))
    # zfill(n) n개의 공간을 확보하고 사용되지 않은 공간만 0으로 채움

'''
대기번호 :001
대기번호 :002
대기번호 :003
...
대기번호 :019
대기번호 :020
'''

answer = input("아무 값이나 입력하세요 :")
# 참고 : 사용자에게 직접 값을 입력 받을 경우에는 숫자로 입력해도 문자로 인식함
print("입력하신 값은 " + answer + "입니다.")
'''
아무 값이나 입력하세요 :>? 10
입력하신 값은 10입니다.

아무 값이나 입력하세요 :>? 오늘은 금요일
입력하신 값은 오늘은 금요일입니다.
'''

# 8-2 다양한 출력포맷
# 8-3 파일입출력
# 8-4 pickle
# 8-5 with
# 8-6 퀴즈 #7
