'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''

import random

a = [0, 0, 0]

print('===[2023-03-08(수)]===')

i = 0
total = 0
while True:

	r = random.randint(1, 10)

	isDuplicate = False

	j = 0
	while j < i:
		if r == a[j]:
			isDuplicate = True
		j += 1

	if isDuplicate == False:
		a[i] = r
		i += 1
		total += r

	if i == len(a) and total == 20:
		break
	elif i == len(a) and total != 20:
		i = 0
		total = 0

print(a)