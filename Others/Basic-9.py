"""
https://www.youtube.com/watch?v=kWiCuklohdY&t=3s

나도코딩
파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]

2022-07-20 03:38:08 ~
"""

# 9-1 클래스
# 스타크래프트 테란
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 9-2 __init__
# 생성자
# 객체를 생성할 때 생성자 옆에 정의된 멤버 변수의 갯수를 충족해야함

'''
예를 들어
marine3 = Unit("마린") 
이렇게 name만 충족시킨채로 생성하는 것은 불가능함.
'''

# 9-3 멤버 변수
# 클래스 내의 변수들 예) name, hp, damage

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True


if wraith2.clocking:  # wraith2.clocking == True: 와 같은 표현
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

'''
변수가 클래스 내부에 없어도 이처럼 외부에서 따로 추가해서 만들 수 있음.
예) wraith2.clocking = 
다만 wraith2에 직접적으로 따로 추가해준 것이기 떄문에 
해당 객체 외에는 적용 불가능함
예) wraith1은 클로킹 관련 적용 불가
      AttribueError: 'Unit' object has no attribute 'clocking'
'''

# 9-4 메소드


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 9-5 상속
# 위의 두개 클래스 중복 부분을 상속받게해 좀 더 간단하게 만들 예정

# 일반 유닛 (부모 클래스)


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 공격 유닛 (자식 클래스)


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 9-6 다중 상속
# 부모가 여럿일 때 다중 상속이라고 함
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃/ 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __int__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 9-7 메소드 오버라이딩
# 9-8 pass
# 9-9 super
# 9-10 스타크래프트 프로젝트 전반전
# 9-11 스타크래프트 프로젝트 후반전
# 9-12 퀴즈 #8