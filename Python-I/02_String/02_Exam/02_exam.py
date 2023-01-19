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
token = origin_str.split(sep = ',')
sent = ' '.join(token)
print('토큰 :',token)
print('문장 :', sent)