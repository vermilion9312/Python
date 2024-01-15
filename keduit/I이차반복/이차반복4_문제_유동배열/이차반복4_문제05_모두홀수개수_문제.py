'''
	[문제]
		(1) 랜덤(1 ~ 9) 사이의 랜덤값을 4개를 저장 후 비교한다. 
		(2) 4개의 랜덤값이 모두 홀수이면 1을 total에 추가,
			하나라도 홀수가 아니면 2를 total에 추가한다.
		(3) (1~2)를 5번 반복한다. 

		[예시] 
			[3, 1, 5, 1] 모두홀수 => total = [1]
			[5, 2, 1, 4] 모두홀수x => total = [1,2]
			...
'''
import random

print('===[2023-03-07(화)]===')

total = []
for __ in range(5):
	
	randomList = []
	for _ in range(4):
		r = random.randint(1, 9)
		randomList.append(r)
	print(randomList, end=" ")

	oddCheck = True
	for v in randomList:
		if v % 2 == 0:
			oddCheck = False

	if oddCheck:
		total.append(1)
		print("모두홀수 => total =", total)
	else:
		total.append(2)
		print("모두홀수x => total =", total)





	

