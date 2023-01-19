"""
chap04_DataStructure
step03_tuple
"""

'''
tuple 특징
- 형식) 변수 = (값1, 값2,...) : 리스트 - 대괄호 / 튜플 - 소괄호
- 순서 존재 (색인 사용 가능)
- 수정 불가 (기존의 만들어진 객체만 사용 가능) : 추가, 삭제, 수정, 삽입 불가
        - 수정을 원할 경우 list로 만들어야 함. 
        - 자체적으로는 불가. 읽기 전용이라고 생각하면 됨.
'''

lst = [10]
type(lst) # list 

# tuple
tp = (10,) # tuple(10,0)랑 같은 말. 즉 소괄호 만으로도 튜플인지 알 수 있음. 
# 주의 : 원소 한개여도 콤마를 넣어줘야 정상적으로 생성. 
tp = 10 # 콤마를 넣어주지 않으면 튜플이 아니라 tp=10 즉 int형과 같게 됨.
print(tp) # (10,)
type(tp) # tuple

tp2 = (1,2,3,4,5)
print(tp2)

print(len(tp2), type(tp2)) # 5 <class 'tuple'>

# indexing : list와 동일
print(tp2[0], tp2[1:4]) # 1 (2, 3, 4)
print(tp2[-1], tp2[-3:]) # 5 (3, 4, 5)


# 수정 불가
tp2[0] = 100 
# TypeError: 'tuple' object does not support item assignment

# tuple -> list 변환
lst =list(tp2)
lst[0]= 100
print(lst) 
# [100, 2, 3, 4, 5]
# 튜플이 수정,삭제가 불가능하므로 리스트로 변환해서 진행해야 함.

# 객체 제거  
del tp2
print(tp2) 
# name 'tp2' is not defined


# for + tuple
datas = (10, 23.4, 6, 8)

for d in datas :
    print(d*2, end = ' ')

# 20 46.8 12 16 
# 이건 튜플 자체를 수정하는 것이 아니라
# 튜플의 원소들을 꺼내서 연산하게 하는 것이므로 가능함. 

# zip() : 내장함수 vector 원소 묶음 -> tuple 반환
names = ['hong', 'lee', 'kang']
pays = [100, 150, 200]

zip_re= zip(names,pays)    
zip_re #  <zip at 0x29bf6463440>

for z in zip_re : 
    print (z)    
'''
('hong', 100)
('lee', 150)
('kang', 200)

zip으로 튜플 결합해놓은 경우 
리스트로 변환하지 않은 상태에서는 이렇게 포문으로 값을 볼 수 있음.

하지만 포문 전에 리스트로 변환했다면 - zip_re2 = list(zip(names, pays))
zip의 자료들을 리스트가 다 가져가 버려서 
호출해도 값이 안나옴.
'''    

# zip -> list 변환  
zip_re2 = list(zip(names, pays))
print(zip_re2)
# [('hong', 100), ('lee', 150), ('kang', 200)]

type(zip_re2) # list
type(zip_re2[0]) # tuple

zip_re2[0] # ('hong', 100)