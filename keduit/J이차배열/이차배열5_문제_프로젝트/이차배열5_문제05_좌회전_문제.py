'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 좌회전시키시오.
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9
        j + 3i - 3

        3 6 9 
        2 5 8 
        1 4 7 
        3j -i + 1

        9 8 7 
        6 5 4 
        3 2 1
        -j  -3i + 13

        7 4 1 
        8 5 2 
        9 6 3 
        -3j + i + 9
'''
import random

block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = random.randint(1, 4)
print("rNum =", r)

for m in range(r):
    
    for i in range(3):
        i += 1
        for j in range(3):
            j += 1
            if m == 0:
                k = j + 3*i - 3
            if m == 1:
                k = 3*j -i + 1
            if m == 2:
                k = -j -3*i + 13
            if m == 3:
                k = -3*j + i + 9
            print(k, end = " ")
        print()
        
    if m != r - 1:
        print()