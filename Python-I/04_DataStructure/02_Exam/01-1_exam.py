'''
문) 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.

lst = [10, 1, 5, 2]

 << 출력 결과 >>
단계1 : [10, 1, 5, 2, 10, 1, 5, 2]
단계2 : [10, 1, 5, 2, 10, 1, 5, 2, 20]
단계3 : [1, 2, 1, 2]
'''

lst = [10, 1, 5, 2]

result = lst * 2
print('단계1 :', result)

result.append(result[0]*2)
print('단계2 :', result)


result2 = result[1::2]
print('단계3 :', result2)