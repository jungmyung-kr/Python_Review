
"""
chap04_DataStructure
step02_list_for
"""

'''
리스트 내포 (함축)
 - list안에서 for와 if문을 한 줄로 표현한 문법

 형식1) 변수 = [실행문  for 변수 in 열거형객체] 
      실행순서 : 1) in 열거형 객체에서 for문 적용 2) for문을 통해 실행문 적용 3) 변수 저장
 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]   
      실행순서 : 1) for 문 2) if 문 [3) 참 :실행문, 거짓: 처음오로 다시 돌아가 4) 변수 저장 ]
'''


# 형식1) 변수 = [실행문  for 변수 in 열거형객체] 

# x변량에 제곱(**) 계산 예
x = [2, 4, 1, 5, 8]

print(x ** 2) 
# TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# list 객체 대상 산술 연산 불가능

# 방법 1) list + for 예   
lst = [] # 빈 list.  계산결과 저장 
for i in x :
    lst.append(i**2) # 각 원소 산술연산 가능

lst # [4, 16, 1, 25, 64]


# 방법 2) list 내포 
lst = [i ** 2 for i in x]
print(lst)

# 각 원소 -> 짝수 or 홀수
result = ['짝수' if i%2 == 0 else '홀수' for i in x]
print(result)
# ['짝수', '짝수', '홀수', '홀수', '짝수']

'''
위의 코드는 간결하게 한줄로 쓴것
한줄씩 쓰려면 아래처럼
result = []
for i in x :
    if i%2 ==0 :
    result.append('짝수')
    else 
    result.append('홀수')
print(result)
'''

# 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]
# if 조건식을 일종의 필터라고 생각하면 됨
# 만족하는 경우에만 실행 

dataset = list(range(1, 101)) 
print(dataset) # 1~100

#  list+for : 10배수 값 저장  
result = [] # 빈 list

for data in dataset :
    if data % 10 == 0 :
        result.append(data)
        
print(result) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]       

# list 내포 : 10배수 값 저장 
result = [data for data in dataset  if data % 10 == 0]
print(result)
# 위의 코드를 간결하게 한줄로 정리한 것.

# 내장함수 사용
min(x) # 최솟값 반환 : 1 
max(x) # 최댓값 반환 : 8
sum(x) # 전체 원소 합 반환 : 20
# mean(x) : error 