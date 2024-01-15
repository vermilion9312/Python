'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''

print('===[2023-03-08(수)]===')

import random
com = [0, 0, 0]
me = [0, 0, 0]

def getList(arr):
	i = 0
	while i < len(arr):
		
		r = random.randint(1, 9)

		isDuplicate = False
		j = 0
		while j < i:
			if arr[j] == r:
				isDuplicate = True
				break
			j += 1

		if isDuplicate == False:
			arr[i] = r
			i += 1

	return arr


com = getList(com)

while True:

	strike = 0
	ball = 0
	me = getList(me)

	for i in range(len(com)):
		for j in range(len(me)):
			if com[i] == me[j]:
				ball +=1
				if i == j:
					strike += 1

	print("com:", com)
	print("me:", me, ", ball:", ball, ", strike:", strike)
	print()

	if strike == len(com):
		break


