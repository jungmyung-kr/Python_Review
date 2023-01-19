"""
chap04_DataStructure
step05_dict
"""

'''
dict 특징 
형식) {key1:value1, key2:value2, ...}
        키와 밸류 한 쌍이 :라는 구분자로 엮인 하나의 원소
- key 이용 -> 수정, 삭제, 추가 
- key 중복 불가능 (key1, key1 - 불가)
- 순서가 없음 - 숫자 색인 불가능
- 따라서 key를 색인으로 사용 (기존은 색인을 순번을 이용했는데 dict형은 유일하게 key사용)
    예) dict객체[key]
'''

# 1. dict 생성 

person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) 
# {'name': '홍길동', 'age': 35, 'addr': '서울시'}
print(len(person), type(person)) 
# 3 <class 'dict'>

    # 키를 색인으로 사용하는 방법 
    person['name'] # '홍길동'


# 2. 수정, 삭제, 추가, 검색 

person['age'] = 45 # 수정 {'name': '홍길동', 'age': 45, 'addr': '서울시'}
del person['addr'] # 삭제 {'name': '홍길동', 'age': 45}
person['pay'] = 350 # 추가 {'name': '홍길동', 'age': 45, 'pay': 350}

'age' in person #  True 
'addr' in person # False

# 3. for + dict

for key in person.keys() : # key 넘김 
    print(key, end = ' ') # key
    print(person[key]) # value
'''
name 홍길동
age 45
pay 350
'''
    
for value in person.values() :  # value 넘김 
    print(value) 
'''
홍길동
45
350
'''

for item in person.items() : # key+value
    print(item)
'''
key, value가 tuple로 묶여서 나옴
('name', '홍길동')
('age', 45)
('pay', 350)
'''
for k,v in person.items() : # key+value
    print(k,'->',v)
'''
튜플로 묶어서 보는게 아니라 각각 구분해서 받고 싶다면
for 다음에 변수를 두개로 분리해주면 됨.
name -> 홍길동
age -> 45
pay -> 350
'''


# key 검색 
print('age' in person) # True    


# 4. 단어 빈도수 
charset = ['pay', 'name', 'pay', 'name', 'age']
charset # list = 중복값 가능
len(charset) # 5

# 방법1) key 검색 

wc = {} # 빈set or 빈 dict / 단어가 key , 빈도수가 value가 되도록 구조 짬.

for ch in charset :
    if ch not in wc : # 사전에 key 유무 
        wc[ch] = 1 # key 없음.
    else :
        wc[ch] += 1 # key 있음 
print(wc) 
# {'pay': 2, 'name': 2, 'age': 1}

# key가 될 charset의 단어가 없으면 새로 넣으면서 빈도 1 (초기 값)
# 그 단어가 이미 들어가 있으면 기존 빈도에 1 추가 

# 방법2) get 메서드 이용
wc.get('pay') #  2  : key를 통해서 value 값을 꺼내는 방식을 사용 
wc.get('lee') # 없는 키를 넣을 경우 : 오류는 아니지만 리턴값이 없음
# 형식) get(key, default=None, /)


wc = {} # 빈set or 빈 dict

for ch in charset :
    wc[ch] = wc.get(ch, 0) + 1  
print(wc) # {'pay': 2, 'name': 2, 'age': 1}

    #  wc에 charset의 키가 없으면, 0으로 값을 초기화 시키고 1을 더한다 
    # 키가 이미 있으면 그 벨류값을 꺼내오고 괄호 밖 +1 만 진행
    # (기존에 1개 였으면 ,뒤의 0 초기화 기능은 실행되지 않고)   
    # 같은 뜻이라 함 wc['pay'] = 1                            
help(wc.get)
#  Return the value for key if key is in the dictionary, else default.



# 5. {key : [value1, value2, ...]}
# 예) {'사번' : [급여, 수당]}
# []안의 부분은 색인 사용 가능하므로 '급여' 부분만 조회하는 것도 가능함 

emp = {'1001' : [250, 50], '1002' : [200, 40], '1003': [300, 80]}

# 급여가 250 이상이면 사번 출력 & 수당 합계 
su_tot = 0 # 수당 합계 

for eno, pay_su in emp.items() : # key + value
    if pay_su[0] >= 250 : # pay_su에서 0번째 원소인 급여 이용 
        print(eno) # 사번 출력 
        su_tot += pay_su[1] # 수당 누적 
print('수당의 합계 : %d'%su_tot) 

'''
1001
1003
수당의 합계 : 130
'''

# key 이용 연산 : 급여 + 보너스 
pay = {'홍길동' : 200, '이순신' : 250, '유관순' : 200} 
bonus = {'홍길동' : 50, '이순신' : 80, '유관순' : 30} 

pays = [pay[k] + bonus[k] for k in pay.keys()] # list 내포
# ex ) pay의 key인 '홍길동'의 value들 = pay 200 / bonus 50 두개가 합쳐져 pays에 저장됨.   
pays # [250, 330, 230]

avg = sum(pays) / len(pays)
print('급여 평균 =', avg) # 급여 평균 = 270.0


# 6. key의 값을 list로 추가
weather =  {} # {'지역명':[최저온도, 최고온도]}

cities = ['서울', '부산', '대구'] # 지역
temps = [10, 30, 15, 35, 20, 40] # 온도 : 서울 최저, 최고 / 부산 최저, 최고 이런 순 

# 1) 2) 메서드 제외 코드 다 동일 / 출력 결과 약간 다름

# 1) append 사용했을 때 

for i in range(len(cities)) : # range(3)
    weather[cities[i]] = [] # {'서울':[], '부산':[], '대구':[] } / 순차적으로 저장됨
    weather[cities[i]].append(temps[i*2:i*2+2]) 
print(weather) # {'서울': [[10, 30]], '부산': [[15, 35]], '대구': [[20, 40]]}
    
# 2) extend 사용했을 때    
for i in range(len(cities)) : # range(3)
    weather[cities[i]] = [] # {'서울':[], '부산':[], '대구':[] } / 순차적으로 저장됨
    weather[cities[i]].extend(temps[i*2:i*2+2])
print(weather) # {'서울': [10, 30], '부산': [15, 35], '대구': [20, 40]}

'''
마땅히 명령을 넣을게 없는데 안넣으면 오류나므로 이럴 때는  pass 사용
for i in range(len(cities)) : # range(3)
    pass
else :
    pass
'''


'''
인덱스 수식써서 사용한 과정 설명
cities index = i = 0,1,2
temp index = 0:2, 2:4, 4:6
    start index = i*2 (즉 시티 인덱스에 *2하면 템프 인덱스 시작값임)
    stop index = city index *2 + 2
'''


# 7. 더미 변수

# 1) 혈액형 더미 변수 
map_data = {'AB':1, 'A':0, 'B':0, 'O':0} # dict
datas = ['A','B','A','O','AB','B'] # list

# list 내포
dummy = [map_data[data] for data in datas]
dummy #  [0, 0, 0, 0, 1, 0]

# 2) label 인코딩: y변수 숫자 변환
label_map = {'thin': [1,0,0], 'normal': [0,1,0], 'fat':[0,0,1]} #dict
datas = ['normal', 'fat', 'thin', 'normal'] #list

# list 내포 : one-hot encoding
labels = [ label_map[data] for data in datas]
labels # [[0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]]