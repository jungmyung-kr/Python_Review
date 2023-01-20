"""
문) 다음 origin_data의 각 리스트에 포함된 두 개의 단어를 하나로 묶어서
    pro_data 리스트에 추가한 후 각 원소를 줄단위로 출력하시오.
    예) ['양말', '신발'] -> ['양발 신발']

<출력결과> 
양말 신발
강아지 고양이
대한민국 수도 서울
"""

origin_data = [['양말', '신말'], ['강아지', '고양이'], ['대한민국', '수도', '서울']]

pro_data = [] # 처리 결과 저장 list

for d in origin_data : 
    token = ' '.join(d)
    pro_data.append(token)
    # print(token)


# for문 밖에서 print(pro_data) 하면 줄 단위로 출력되지 않고 리스트 나열되므로 
# for문 안에서 token 출력해야함.
