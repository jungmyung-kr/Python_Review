"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-20 03:38:08 ~ 04:09:28
2022-07-21 04:09:29 ~ 04:50:12
"""

# 스타크래프트

from random import *

# 일반 유닛 (부모 클래스)


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1}시 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛 (자식 클래스)


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 마린


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)"\
                  .format(self.name))
        else:
            print("{0) : 체력이 부족하여 스팀팩을 사용하지 않습니다."\
                  .format(self.name))


# 탱크


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developed:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if not self.seize_mode:
            print("{0} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 핸재 시즈모드 일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈 모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 날 수 있는 기능을 가진 클래스

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")  # good game
    print("[Player]님이 게임에서 퇴장하셨습니다.")


# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 ( 생성된 모든 유닛 append)
attack_units = [m1, m2, m3, t1, t2, w1]

# 전군 이동
for unit in attack_units:
    unit.move("1")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이즈 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()


'''[알림] 새로운 게임을 시작합니다.
마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
탱크 유닛이 생성되었습니다.
탱크 유닛이 생성되었습니다.
레이스 유닛이 생성되었습니다.
마린 : 1시 방향으로 이동합니다. [속도 1]
마린 : 1시 방향으로 이동합니다. [속도 1]
마린 : 1시 방향으로 이동합니다. [속도 1]
탱크 : 1시 방향으로 이동합니다. [속도 1]
탱크 : 1시 방향으로 이동합니다. [속도 1]
레이스 : 1시 방향으로 날아갑니다. [속도 5]
[알림] 탱크 시즈 모드 개발이 완료되었습니다.
마린 : 스팀팩을 사용합니다. (HP 10 감소)
마린 : 스팀팩을 사용합니다. (HP 10 감소)
마린 : 스팀팩을 사용합니다. (HP 10 감소)
탱크 : 시즈 모드로 전환합니다.
탱크 : 시즈 모드로 전환합니다.
레이스 : 클로킹 모드 설정합니다.
마린 : 1시 방향으로 적군을 공격합니다. [공격력5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력5]
탱크 : 1시 방향으로 적군을 공격합니다. [공격력70]
탱크 : 1시 방향으로 적군을 공격합니다. [공격력70]
레이스 : 1시 방향으로 적군을 공격합니다. [공격력20]
마린 : 9 데미지를 입었습니다.
마린 : 현재 체력은 21입니다.
마린 : 18 데미지를 입었습니다.
마린 : 현재 체력은 12입니다.
마린 : 11 데미지를 입었습니다.
마린 : 현재 체력은 19입니다.
탱크 : 14 데미지를 입었습니다.
탱크 : 현재 체력은 136입니다.
탱크 : 14 데미지를 입었습니다.
탱크 : 현재 체력은 136입니다.
레이스 : 9 데미지를 입었습니다.
레이스 : 현재 체력은 71입니다.
Player : gg
[Player]님이 게임에서 퇴장하셨습니다.
'''

# 퀴즈 #8

'''
Quiz) 주어진 코드를 활용하여 브동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass
'''


class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses = [house1, house2, house3]

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
