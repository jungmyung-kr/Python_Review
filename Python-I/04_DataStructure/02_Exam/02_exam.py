'''
문1) message에서 'spam' 원소는 1, 'ham' 원소는 0으로 dummy 변수를 생성하시오.

<조건> 
list + for 형식 적용   

<출력결과>      
[1, 0, 1, 0, 1]   

lst = [i ** 2 for i in x]

result1 = ( 1 if msg =='spam else 0 for msg in message )
'''



message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy = []
dummy = [1 if msg == 'spam' else 0 for msg in message]
print(dummy)

'''
문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.

<조건> 
list + for + if 형식2) 적용   

<출력결과>      
['spam', 'spam', 'spam']   
'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list = [msg for msg in message if msg =='spam']
print(spam_list)




