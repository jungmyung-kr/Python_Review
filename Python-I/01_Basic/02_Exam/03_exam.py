'''
문3) 화씨를 섭씨로 변환하는 프로그램을 작성하시오.
   화씨온도 변수명 : ftemp
   섭씨온도 변수명 : ctemp
   온도변환 수식 = (화씨온도 - 32.0) * (5.0/9.0)
   
   <<화면출력 결과>>
 화씨온도 : 93
 섭씨온도 = 33.888889
'''

ftemp = float(input('화씨온도 :'))
ctemp = (ftemp - 32.0) * (5.0/9.0)
print('섭씨 온도 = ', ctemp)