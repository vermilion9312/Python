'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		6 5 4
		5 4 3
		4 3 2
		3 2 1
'''

print('===[2023-01-29 (일)]===')
import random
row = random.randint(3, 6)
print("r =", row)

print()
print("===[일차반복문]===")

for i in range(row - 2):
	col = (-1) * i + 6
	print(col)

print()
print("===[이차반복문]===")

for i in range(row - 2):
	col = (-1) * i + 6
	for j in range(3):
		print(col)