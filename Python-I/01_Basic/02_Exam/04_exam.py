
''' 
문4) 지방(fat), 탄수화물(carbohydrate), 단백질(protein)            
       칼로리의 합계를 계산하는 프로그램을 작성하시오.
    조건1> 지방, 탄수화물, 단백질의 그램을 키보드로 입력받음 
    조건2> 3개 데이터 이용 총 칼로리 계산
               총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4              
    조건3> 총 칼로리 출력 : format()함수 이용 
    
   <<화면출력 결과>>
  지방의 그램을 입력하세요 : 25
  탄수화물의 그램을 입력하세요 : 520
  단백질의 그램을 입력하세요 : 45
  총칼로리 : 2,485 cal
'''

fat = int(input('지방의 그램을 입력하세요 :'))
carbohydrate = int(input('탄수화물의 그램을 입력하세요'))
protein = int(input('단백질의 그램을 입력하세요'))
calories = fat * 9 + protein * 4 + carbohydrate * 4
print('총칼로리 :', format(calories,'3,'),'cal')