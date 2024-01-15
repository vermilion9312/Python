'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		4 5 6
		7 8 9
	    10 11 12
        13 14 15
	    16 17 18
 	[예시2]
		r = 3
	[출력2]
		1 2 3
		4 5 6
		7 8 9	
'''

import random
print("===[2023-01-28 (토)]===")
row = random.randint(3, 6)
print("r =", row)

print("===[일차반복문]===")
for i in range(row):
    col = 3 * i + 1
    print(col + 0, col + 1, col + 2)

print("===[이차반복문]===")
for i in range(row):
    col = 3 * i + 1
    for j in range(3):
        col += j
        print(col, end = " ")
    print()

# print("===[정답풀이]===")
# import random

# r = random.randint(3, 6)
# print(r)

# for i in range(r):
#     a = i * 3 + 1
#     print(a + 0, a + 1 , a + 2)

# print("----")
# for i in range(r):
#     a = i * 3 + 1
#     for j in range(3):
#         print(a + j, end=" ")
#     print()
