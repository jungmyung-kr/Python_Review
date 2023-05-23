# 딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않음
# key를 통해 value를 찾음
# {Key1 : Value1, Key2 : Value2, Key3 : Value3, ...}

dic = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}

a = {1 : 'hi'} # Key에 숫자 입력 가능 / Value에 문자열 입력 가능 

a = {'a':[1, 2, 3]} # Value에 리스트도 넣을 수 있음. 

# 딕셔너리 쌍 추가하기 

a = {1 : 'a'} 

a[2] = 'b' # {2 : 'b'}쌍 추가 : key : 2, value : 'b'
a # {1: 'a', 2: 'b'}

a['name'] = 'pey' 
a # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
a # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기 

del a[1] # key가 a인 key:value 쌍 삭제 
a # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리에서 Key 사용해 Value 얻기 
# 딕셔너리에서의 a[0]과 리스트,튜플에서의 a[0]는 다르다. 
# 리스트,튜플에서의 a[0] : 변수 a의 0번째 요소 
# 딕셔너리에서의 a[0] : 변수 a의 key가 0인 value

grade = {'pey': 10, 'julliet' : 99}
grade['pey'] # 10 
grade['julliet'] # 99


# 주의 사항 

# 주의 사항 1 
# : 중복된 key가 있을 경우, 1개를 제외하고 나머지가 무시됨

a = {1 : 'a', 1: 'b'}
a # {1: 'b'}

# 주의 사항 2 
# : key에는 리스트를 쓸 수 없음, 튜플은 사용할 수 있음.
# key는 변하지 않아야 함. 리스트와 달리 튜플은 값이 변하지 않으므로, key로 사용 가능 

# value에는 상관없음! 숫자, 문자열, 튜플, 리스트 다 가능  

a = {[1,2] : 'hi'} # TypeError: unhashable type: 'list'

# key 리스트 만들기 

a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
a.keys() # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)
# name
# phone
# birth

list(a.keys()) # 딕셔너리의 key를 리스트화 하고 싶을 때 
# ['name', 'phone', 'birth']

# value 리스트 만들기 

a.values() # dict_values(['pey', '0119993323', '1118'])

# key, value 쌍 얻기

a.items()
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# key:value쌍 모두 지우기 

a.clear()
a # {}

# key로 value 얻기 
a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}

a.get('name') # 'pey'
a.get('phone') # '0119993323'
# a['name'], a['phone']과 같은 결과 반환 

# 그렇다면 a[]와 a.get() 차이점은?

print(a.get('nokey')) # None
print(a['nokey']) # KeyError: 'nokey'

# 즉, get은 존재하지 않는 키일 경우 none을 반환 / []는 오류 발생

# 찾으려는 key값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하려면? 

a.get('foo', 'bar') # 'bar'
# get(x, '디폴트 값')

a.get('nokey', 'dict a doesn\'t have that key')
# "dict a doesn't have that key"

# 해당 key가 딕셔너리 안에 있는지 조사하기 

a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}

'name' in a # True

'email' in a # False