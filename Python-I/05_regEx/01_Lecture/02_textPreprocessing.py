"""
Chap05_regEx
step02_text_preprocessing
텍스트 전처리 : 특수문자, 불용어 처리 
"""

import re # re 모듈 가져오기 

# 전처리 텍스트  
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']
type(texts) #list
type(texts[-1]) #str

texts.lower() # AttributeError: 'list' object has no attribute 'lower'
texts[-1].lower() #'uysfsfa,  a124&***$?'

# 리스트에 문자에 적용하는 메서드 사용하면 적용안됨. 인덱스로 지정해주고 써야함.

# 단계1 : 소문자 변경 

# list 내포 : 변수 = [실행문 for]
# lower는 소문자 = 문자형이여야 적용가능, 리스트에는 불가 

texts_re = [ st.lower() for st in texts]
print(texts_re)
# ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,  a124&***$?']
'''
texts_re = []
for st in texts :
    texts_re.append(st.lower())
'''

# 단계2 : 숫자 제거 : sub('pattern', rep, string)
# texts_re에서 10진수 정수를 ''로 대체 => 제거
texts_re2 = [re.sub('[0-9]', '', st) for st in texts_re]
print(texts_re2)
# ['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,  a&***$?']


# 단계3 : 문장부호 제거 
punc_str = '[,.?!:;]' # 이렇게 변수에 다 넣어도 되고,  sub문에 직접 다 써줘도 됨.
texts_re3 = [re.sub(punc_str, '', st) for st in texts_re2]
print(texts_re3)
# ['afabasabag', 'abtta $$a', 'uysfsfa  a&***$']

# 단계4 : 특수문자 제거 
spec_str = '[@#$%^&*()]'
texts_re4 = [re.sub(spec_str, '', st) for st in texts_re3]
print(texts_re4)
# ['afabasabag', 'abtta a', 'uysfsfa  a']

# 단계5 : 공백 제거 (white space) : 2칸 이상 공백 -> 1칸
texts_re5 = [' '.join(st.split()) for st in texts_re4] # 'uysfsfa  a' -> 'uysfsfa a'
print(texts_re5)
# ['afabasabag', 'abtta a', 'uysfsfa a']