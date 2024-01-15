'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 7 13
		2 8 14
		3 9 15
		4 10 16
		5 11 17
		6 12 18
 	[예시2]
		r = 3
	[출력2]
		1 4 7
		2 5 8
		3 6 9	
'''

import random
print("===[2023-01-28 (토)]===")
row = random.randint(3, 6)
print("r =", row)

print("===[일차반복문]===")
for i in range(row):
    col = i + 1
    print(col + 0 * row, col + 1 * row, col + 2 * row)

print()
print("===[이차반복문]===")
for i in range(row):
	col = i + 1
	for j in range(3):
		print(col + j * row, end = " ")
	print()




# print("===[정답풀이]===")
# import random

# r = random.randint(3, 6)
# print(r)
# for i in range(r):
#     a = i + 1
#     print(a + r * 0, a + r * 1 , a + r * 2)

# print("----")
# for i in range(r):
#     a = i + 1
#     for j in range(3):
#         print(a +  j * r, end=" ")
#     print()
