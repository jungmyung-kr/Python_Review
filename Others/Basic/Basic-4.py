"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-11 00:46:57 ~ 01:22:30
"""

# 4-1 문자열

sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 4-2 슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7])  # 성별 : 1
print("연 : " + jumin[0:2])  # 연 : 99
print("월 : " + jumin[2:4])  # 월 : 01
print("일 : " + jumin[4:6])  # 일 : 20

print("생년월일 : " + jumin[:6])  # 생년월일 : 990120
print("뒤 7자리 : " + jumin[7:])  # 뒤 7자리 : 1234567
print("뒤 7자리 : " + jumin[-7:])  # 뒤 7자리 : 1234567

# 4-3 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())  # python is amazing
print(python.upper())  # PYTHON IS AMAZING
print(python[0].isupper())  # python 변수의 0번째 글짜가 대문자인지 물음 : True
print(len(python))  # 문자열 길이 : 17
print(python.replace("Python", "Java"))  # 인쇄용이기 때문에 실제 변수는 바뀌지 않음

index = python.index("n")
print(index)  # 5번째
index = python.index("n", index+1)
print(index)  # 두번째 n 찾기 : 15번째

print(python.find("Java"))  # find에서는 원하는 값이 없을 경우 -1 반환
print(python.index("Java"))  # index에서는 원하는 값이 없을 경우 에러 반환

# 4-4 문자열 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20)  # d는 정수값만 가능
print("나는 %s을 좋아해요." % "파이썬")  # s는 문자열
print("Apple은 %c로 시작해요." % "A")  # c는 문자열 한 글자
# %s
print("나는 %s살입니다." % "20")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))  # 나는 빨간색과 파란색을 좋아해요.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20)) # 변수 순서 바꿔도 무방

# 방법 4 (v3.6이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 4-5 탈출 문자
# \n : 줄 바꿈
print("백문이 불여일견 \n백견이 불여일타")
'''
백문이 불여일견 
백견이 불여일타
'''

# 저는 "나도 코딩" 입니다.
# 방법1 : 따옴표 두 종류
print('저는 "나도 코딩"입니다.')

# 방법2 : 탈출문자 \
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
# print("C:\Users\Myung\Desktop\Python_Review") : 오류 발생
print("C:\\Users\\Myung\\Desktop\\Python_Review")  # C:\Users\Myung\Desktop\Python_Review

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine')  # PineApple : \r뒤의 글자수만큼 맨 앞으로 이동해 대체

# \b : 백스페이스 : 한 글자 삭제
print("Redd\bApple")  # RedApple : \b앞 한 글자 삭제

# \t : 탭
print("Red\tApple")  # Red	Apple

# 4-6 퀴즈 #3
'''
Quiz) 사이즈별로 비밀번호를 만들어주는 프로그램을 작성하시오.

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯 수 + "!"로 구성
                                nav                 5               1                    !
예) 생성된 비밀번호 : nav51!
'''

# url = "http://daum.net"
# url = "http://naver.com"
# url = "http://google.com"
url = "http://youtube.com"

pw = url.replace("http://","")
pw = pw[:pw.index(".")]
pw = (pw[:3] + str(len(pw)) + str(pw.count("e")) + "!")

print("{0}의 비밀번호는 {1}입니다.".format(url, pw))
# http://youtube.com의 비밀번호는 you71!입니다.