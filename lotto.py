import random
 
gen_count = 5  # 생성할 개수
 
arr = [x for x in range(1, 46)]  # 1부터 45까지 생성
for x in range(0, gen_count):
    random.shuffle(arr)     # 섞기
    arr_selected = arr[:6]  # 6개만 선택
    arr_selected.sort()     # 선택된 번호를 정렬
    print(arr_selected) 
