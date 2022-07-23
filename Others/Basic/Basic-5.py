"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-11 01:22:31 ~ 01:57:32
"""

# 5-1 리스트 []
# 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
# 이렇게 각 변수에 넣는 방법도 있지만 순서를 가지는 리스트로 변수 하나에 넣기도 있음

subway = [10, 20, 30]

# 기차 승객
train = ['유재석', '박명수', '조세호']

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(train.index('조세호'))  # 2

# 하하씨가 다음 역에서 다음 칸에 탐
train.append('하하')
print(train)  # ['유재석', '박명수', '조세호', '하하']

# 정형돈씨가 유재석 / 박명수 사이에 태워봄
train.insert(1, '정형돈')  # 위치 인덱스, 추가할 문구
print(train)  # ['유재석', '정형돈', '박명수', '조세호', '하하']

# 기차에 있는 사람을 한 명씩 뒤에서 꺼냄
print(train.pop())  # 하하가 빠짐
print(train)  # 남은 사람 : ['유재석', '정형돈', '박명수', '조세호']

# 같은 이름의 사람이 몇 명 있는지 확인
train.append('유재석')
print(train)
print(train.count('유재석'))  # 2

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)  # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)  # []

# 다양한 자료형 함께 사용
mix_list = ['조세호', 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)  # [5, 2, 4, 3, 1, '조세호', 20, True]

# 5-2 사전 {}

# 예시 : 목욕탕 개점 , 목욕탕 캐비넷 사용 키 배부

cabinet = {3: '유재석', 100: '김태호'}
# key : value 순서
# key가 반드시 숫자일 필요는 없음

# 값 가져오기 방법 1
print(cabinet[3])  # []에 키 값 넣으면 '유재석' 출력
print(cabinet[100])

# 값 가져오기 방법 2
print(cabinet.get(3))

# 1,2의 차이 []와 get
# 만약에 없는 키를 입력한다면?
print(cabinet[5])  # KeyError가 발생
print(cabinet.get(5))  # None이라고 출력

# 추가 : 없는 값을 가져오려고 했을 때 None 대신 출력 문구 지정 가능
print(cabinet.get(5, '사용 가능한 키입니다.'))

# 특정 key가 해당 변수에 있는지 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# 새 손님
cabinet[3] = '조세호'  # 기존에 키가 존재했다면 값 대체
cabinet[5] = '김종국'  # 없는 키라면 값 추가

print(cabinet)  # {3: '조세호', 100: '김태호', 5: '김종국'}

# 간 손님
del cabinet[3]
print(cabinet)  # {100: '김태호', 5: '김종국'}

# key들만 출력
print(cabinet.keys())  # dict_keys([100, 5])

# value들만 출력
print(cabinet.values())  # dict_values(['김태호', '김종국'])

# key, value 쌍으로 출력
print(cabinet.items())  # dict_items([(100, '김태호'), (5, '김종국')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)  # {}

# 5-3 튜플
# 수정, 추가, 변경 불가능 : 읽기 전용이라고 생각하면 됨.
# 대신 속도가 빠름

# 돈까스 집 메뉴
menu = ('돈가스', '치즈가스')
print(menu[0])
print(menu[1])

# menu.add('생선가스') 불가능 : 튜플은 추가 불가

'''
name = '김종국'
age = 20
hobby = '코딩'
print(name, age, hobby)
이렇게 일일이 변수 입력하는 대신
'''
(name, age, hobby) = ('김종국', 20, '코딩')
print(name, age, hobby)

# 5-4 세트 : 집합
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 (java, python 모두 할 수 있는 개발자)
print(java & python)  # {'유재석'}
print(java.intersection(python))  # {'유재석'}

# 합집합 (java나 python 할 수 있는 개발자)
print(java | python)  # {'박명수', '양세형', '유재석', '김태호'}
print(java.union(python))  # {'박명수', '양세형', '유재석', '김태호'}

# 차집합 (java 할 수 있지만 python  할 수 없는 개발자)
print(java - python)  # {'김태호', '양세형'}
print(java.difference(python))  # {'김태호', '양세형'}

# python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)  # {'유재석', '김태호', '박명수'}

# java를 다 까먹음
java.remove('김태호')
print(java)  # {'유재석', '양세형'}

# 5-5 자료 구조의 변경
# 카페
menu = {'커피', '우유', '주스'}  # set
print(menu, type(menu))  # {'우유', '주스', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu))  # ['우유', '주스', '커피'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))  # ('우유', '주스', '커피') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))  # {'우유', '주스', '커피'} <class 'set'>

# 5-6 퀴즈  #4

'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오. 

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1 
커피 당점차 : [ 2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import * 
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1)) 
'''
from random import *

users = range(1, 21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)  # 4명 중 1명 치킨, 나머지 커피

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('-- 축하합니다. --')

'''
 -- 당첨자 발표 --
치킨 당첨자 : 12
커피 당첨자 : [14, 6, 15]
-- 축하합니다. --
'''