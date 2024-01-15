'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
import random
lotto = []

print('===[2023-02-07 (화)]===')

def getList():
	import random
	lotto = []
	i = 0
	while len(lotto) < 6:
		r = random.randint(1, 45)
		lotto.append(r)
		i += 1
	return lotto


def bubbleSort(list):
	for i in range(len(list) - 1):
		for j in range(len(list) - i - 1):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	print(list)

lotto = getList()
bubbleSort(lotto)