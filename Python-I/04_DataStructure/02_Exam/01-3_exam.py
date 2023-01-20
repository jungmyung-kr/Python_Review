'''
리스트(list)에 추가할 원소의 개수를 키보드로 입력 받은 후, 
    입력 받은 수 만큼 임의 숫자를 리스트에 추가한다. 
    이후 리스트에서 찾을 값을 키보드로 입력한 후 
    리스트에 해당 값이 있으면 "YES", 없으면 "NO"를 출력하시오. 

<출력 예시1>
list 개수 : 5
1
2
3
4
5
3  <- 찾을 값 
YES

<출력 예시2>
list 개수 : 3
1
2
4
3 <- 찾을 값 
NO
'''

size = int(input('list 개수 : ')) 
lst = []
for i in range(size) :
    lst.append(int(input()))
# input 3개 -> 총 3개의 수 리스트에 추가 가능 


if int(input()) in lst :
    print('YES')
else :
    print('NO')
# 임의의 수를 입력했을 때, 리스트 내 3개 숫자 중에 있으면 'YES', 없으면 'NO'











