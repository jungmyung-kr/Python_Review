"""
chap06_Function
step04_func_args
"""

'''
함수의 가변인수 
- 한 개 가인수로 여러 개의 실인수를 받는 인수
'''

# 1. tuple형 가변인수 
def func1(name, *names) :
    print(name) # 홍길동 
    print(names) # ('이순신', '유관순')

func1("홍길동", "이순신", "유관순")


# 2. dict형 가변인수 
def person(w, h, **other) :
    print('몸무게 :', w) # 몸무게 : 65
    print('키 : ', h) # 몸무게 : 65
    print('기타 : ', other)  # 기타 :  {'name': '홍길동', 'addr': '서울시'}   

person(65, 175, name='홍길동', addr = '서울시')


# 3. 함수를 인수로 넘기기  
def square(x) : # x^2
    return x**2

def my_func(func, datas) : # (함수, 데이터셋)
    re = []
    for x in datas :
        re.append(func(x)) # (square(x))
    return re  

datas = [2,4,6]
result = my_func(square, datas)    
print(result) # [4, 16, 36]