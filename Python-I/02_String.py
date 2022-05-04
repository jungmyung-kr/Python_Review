# -*- coding: utf-8 -*-

'''
문1) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 저장 변수 : word1, word2, word3 
  조건2) 입력과 출력 구분선 : * 연산자 이용 
  조건3) 약자 저장 변수 : abbr
  조건4) 원래 단어 저장 변수 : tot_words  
   
   <<화면출력 결과>>  
 첫번째 단어 : Korea 
 두번째 단어 : Baseball
 세번째 단어 : Org
 =================
 약자 : KBO
 원래 단어 : Korea Baseball Orag
'''

word1 = input('첫번째 단어 :')
word2 = input('두번째 단어 :')
word3 = input('세번째 단어 :')

abbr = word1[0] + word2[0] + word3[0]
tot_words = word1 + ' '+ word2 + ' '+word3

print('='*20)
print('약자 :'+ abbr)
print('원래 단어 : ' + tot_words)


###############################################################################


'''
문2)  origin_str의 문자열 객체를 대상으로 다음과 같이 처리하시오.
  단계1) 콤마(,) 기준 토큰(단어) 생성 
  단계2) 생성된 토큰(단어) 출력
  단계3) 토큰을 한 개의 문장으로 결합
   
   <<화면출력 결과>>  
 토큰 : ['책상', ' 의자', ' 서적', ' 대한민국', ' 수도', ' 서울']
 문장 : 책상  의자  서적  대한민국  수도  서울 
'''
origin_str = '책상, 의자, 서적, 대한민국, 수도, 서울'

words = origin_str.split(sep = ',' )
print('토큰 : ', words)

sentence = ' '.join(words)
print('문장 : ', sentence)