"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-22 05:14:23 ~ 06:01:27 (완강)
"""

# 11-1 모듈
'''
아래와 같은 내용으로 theater_module.py 모듈 생성

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원입니다.".format(people, people*10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조할인 가격은 {1}원입니다.".format(people, people*6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인할인 가격은 {1}원입니다.".format(people, people*4000))
'''
# 방법 1
import theater_module

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(2)

# 방법 2 : 모듈 별칭 사용
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(2)

# 방법 3 : 해당 모듈 전체 import
from theater_module import *
price(3)
price_morning(4)
price_soldier(2)

# 방법 4 : 필요한 것만 import
from theater_module import price, price_morning
price(3)
price_morning(4)
price_soldier(2)

# 방법 5 : 필요한 것만 import, 별칭 사용
from theater_module import price_soldier as price
price(5)

# 11-2 패키지
'''
thailand.py 생성

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

vietnam.py 생성

class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")
'''
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

# 11-3 __all__
'''
직접 작성한 모듈의 공개 여부를 개발자가 직접 설정해줘야 함 
그렇지 않을 경우 import *로 폴더 내 모든 모듈을 불러낼 수 없음

__all__ = ["vietnam"] 이렇게 공개해서 저장해준 모듈만 임포트 가능
'''

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 11-4 모듈 직접 실행
'''
thailand.py 모듈의 내용은 다음과 같음.
모듈 내에서 호출할 때 출력되는 문구와
모듈 외부에서 호출할 때 출력되는 문구가 다르게 설정

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to =ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
'''
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 11-5 패키지, 모듈 위치

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# 11-6 pip install

# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print((soup.prettify()))

# pip list : 현재 설치된 패키지 확인 가능
# pip show beautifulsoup4 : 정보 확인 가능
# pip install --upgrade beautifulsoup4  : 패키지 업그레이드
# pip uninstall beautifulsoup4 : 패키지 삭제

# 11-7 내장 함수

# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))
'''
무슨 언어를 좋아하세요?>? 파이썬
파이썬은 아주 좋은 언어입니다!
'''

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

import random  # 외장 함수
print(dir(random))
'''
['BPF', 'LOG4', 'NV_MAGICCONST', 
....
'random', 'randrange', 'sample', 'seed', 'setstate', 
'shuffle', 'triangular', 'uniform', 
'vonmisesvariate', 'weibullvariate']
'''

lst = [1, 2, 3]
print(dir(lst))
'''
...'count', 'extend', 'index', 'insert', 'pop'...
'''

name = "Jim"
print(dir(name))
'''
...'find', 'format', 'index', 'isprintable', 'isspace', 'istitle', 'join'...
'''

# 11-8 외장 함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)

import glob
print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 생성하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
import time
print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=22,
# tm_hour=21, tm_min=3, tm_sec=7, tm_wday=4, tm_yday=203, tm_isdst=0)

print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 2022-07-22 21:03:59

import datetime
print("오늘 날짜는", datetime.date.today(), "입니다.")
# 오늘 날짜는 2022-07-22 입니다.

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today+td, "입니다.")
# 우리가 만난지 100일은 2022-10-30 입니다.

# 11-9 퀴즈 # 10
'''
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오.

조건: 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
'''

import byme
byme.sign()