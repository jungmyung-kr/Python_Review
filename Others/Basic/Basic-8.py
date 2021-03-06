"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-15 02:58:59 ~ 03:10:11
2022-07-16 03:10:12 ~ 03:17:44
2022-07-17 03:17:45 ~ 03:26:26
2022-07-18 03:26:27 ~ 03:30:21
2022-07-19 03:30:22 ~ 03:39:07
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

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리 수까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


# 8-3 파일입출력

# 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 덮어쓰기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 읽기 : 방법 1
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 읽기 : 방법 2
# 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")  # end="" 없으면 문장간 줄 바꿈 존재
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 읽기 : 방법 3
# while 반복문 사용 : file이 총 몇 문장인지 알 수 없을 경우 반복문 사용해 불러오기도 가능
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:  # 더 이상 읽을 문장이 없으면,
        break  # 반복문 탈출
    print(line, end="")
score_file.close()

# 읽기 : 방법 4
# 모든 문장을 list 형태로 저장
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

# 8-4 pickle

import pickle

# 파일 쓰기
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "요리", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile의 내용을 profile_file에 저장
profile_file.close()

# 파일 읽어오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # profile_file에 있는 정보를 불러와 profile에 저장
print(profile)
profile_file.close()

# 8-5 with
# file close()하지 않아도 됨.

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# 8-6 퀴즈 #7

'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X주차 주간 보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt',...와 같이 만듭니다.
'''
for num in range(1, 51):
    with open(str(num) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간 보고 -".format(num))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")