'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''
import random
r = random.randint(2, 100)
print("r =", r)

print('===[2023-02-04 (토)]===')

print("소수 =", end = " ")
count = 0
for i in range(2, r + 1):

	check = True
	j = 2
	while j * j <= i:
		if i % j == 0:
			check = False
		j += 1 

	if check:
		count += 1
		print(i, end = " ")
print()
print("개수 =", count)

