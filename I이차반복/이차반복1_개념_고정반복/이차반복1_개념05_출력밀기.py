'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같이 출력하시오.
		단, 아래 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		2 3 4
		3 4 5
		4 5 6
 	[예시2]
		r = 4
	[출력2]
		1 2 3
		2 3 4		
'''

print("===[2023-01-28 (토)]===")
import random
row = random.randint(3, 6)
print("r =", row)

print()
print("===[일차반복문]===")
for i in range(row - 2):
	col = i + 1
	print(col + 0 * 1, col + 1 * 1 , col + 2 * 1)


print()
print("===[이차반복문]===")
for i in range(row - 2):
	col = i + 1
	for j in range(3):
		print(col + j * 1, end = " ")
	print()















# print("===[정답풀이]===")
# import random

# r = random.randint(3, 6)
# print("r : " , r)
# for i in range(r - 2) :
#     a = i + 1
#     print(a + 0 ,  a + 1 , a + 2)
# print("===============================")

# print("r : " , r)
# for i in range(r - 2) :
#     num = i + 1
#     for j in range(3) : 
#         print(num + j , end=" ")
#     print()

