'''
	[문제]
		석차를 출력하시오.
	[정답]
		2 3 4 1 
'''

numList = [1001, 1002, 1003, 1004]
scoreList = [87, 42,  11, 98]

print('===[2023-03-07(화)]===')

rankList = [len(scoreList) for _ in range(len(scoreList))]

for i in range(len(scoreList)):
	for j in range(len(scoreList)):
		if scoreList[i] > scoreList[j]:
			rankList[i] -= 1

print(rankList)