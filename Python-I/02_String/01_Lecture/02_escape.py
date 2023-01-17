"""
chap02_String
step02_escape
"""

'''
2. escape 문자 
 escape 문자  : 특수기능의 문자(\n, \t, \b, \r, '', "")
 기능 차단: escape 문자의 기능 차단 (콘솔 출력, 파일 경로 사용)
'''

print('escape 문자')
print('\\n출력') # escape 기능 차단 방법1 - \ 
print(r'\n출력') # escape 기능 차단 방법2 - r 

# 경로 표현 
print('c:\python\test') # c:\python	est : escape문자 기능 작동...
print('c:\\python\\test') # c:\python\test : \로 escape 문자 기능 차단
print(r'c:\python\test') # c:\python\test : r로 escape 문자 기능 차단
# 한두개 차단하려면 \를 써주면 되지만 너무 많을 경우 r로 하는게 편할 듯
 
# 문) c:\'aa'\"abc.txt" 형식으로 출력되도록 하시오.
print ("c:\\\'aa\'\\\"abc.txt\"") # c:\'aa'\"abc.txt"


file = open(file=r'C:\ITWILL\4_Python-I\workspace\chap02_String\lecture\test.txt',
     mode='r', encoding='utf-8')

print(file.read())

'''
우리나라 대한민국
나는 홍길동입니다.
'''
file.close()