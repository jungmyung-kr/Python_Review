"""
chap04_DataStructure
step04_set
"""


'''
set 특징 (주머니라고 생각하면 좋음)
 - 순서 없음(색인 사용불가)
 - 중복 허용 불가 
 - 수정 불가(추가, 삭제 가능) : 수정 불가인 이유: 색인 사용이 불가능하므로 
 - 형식) 변수 = {값, 값,...} : 순서 상관없으므로 값1, 값2, ... 대신 값 들의 나열로 표현
'''

# 1. set 생성 
st = {1, 3, 5, 1, 5} # 중복 허용 불가 
print(st, len(st)) 
# {1, 3, 5} 3
# 중복이 허용되지 않으므로 유니크한 값만으로 생성됨.

# for + set
for s in st :
    print(s, end = ' ') # 1 3 5
# 순서 없는 자료임. 자료의 양이 적기때문에 마치 순서가 있게 작업해서 출력한 것 같지만
# 양이 많으면 set은 순서 없다는 것을 확인할 수 있을 것임.

# 색인 사용 불가
st[0] 
# : 'set' object is not subscriptable


# 2. 중복 불가 
gender = ['남','여','남','여'] # list
gender
# ['남', '여', '남', '여']

# list -> set
sgender = set(gender)
print(sgender) 
# {'여', '남'}
# 중복이 불가하므로 중복 제거한 요소들만 출력

sgender[0] # 불가
# 색인 사용하려면 다시 리스트로 형변환해야함

# set -> list
lgender = list(sgender)
lgender[0] # '여'
print(lgender) # ['여', '남']
# set 자체는 순서가 없기 때문에 list로 변환될 때 원래 순서랑 다르게 저장되어 있을 수도 있음
# 원래랑 같다면 그냥 우연의 일치일 뿐임. 


# 집합관련 
set1 = {1, 3, 4, 5, 7}
set2 = {3, 5}

set1.union(set2) #  합집합 : {1, 3, 4, 5, 7}
set1.difference(set2) # 차집합 : {1, 4, 7}
set1.intersection(set2) # 교집합 : {3, 5}

# 원소 추가 
set2.add(7) # append의 경우: 맨 뒤에 추가해주는 기능. set은 순서가 없으므로 해당 기능 대신 add로 실행
print(set2) # {3, 5, 7}

# 원소 삭제 
# discard
set2.discard(7) 
print(set2) # {3, 5}
set2.discard(50) # 없는 원소 제거: 오류메세지 출력 없이 실행은 함.
#remove
set2.remove(5)
print(set2) # {3}
# discard와 동일해보임.. 차이점은?
set2.remove(50) # KeyError: 50. 여긴 에러 출력됨.


# 사용 가능한 메서드 확인
dir(set1)
'''
 'add',
 'clear',
 'copy',
 'difference',
 'difference_update',
 'discard',
 'intersection',
 'intersection_update',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'symmetric_difference',
 'symmetric_difference_update',
 'union',
 'update'
 '''