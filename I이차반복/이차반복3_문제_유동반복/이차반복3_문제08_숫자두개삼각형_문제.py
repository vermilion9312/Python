'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1 2
		1 2 3 4
		1 2 3 4 5 6
		1 2 3 4 5 6 7 8
'''

print('===[2023-02-02 (목)]===')

for i in range(4):
	i += 1
	for j in range(2 * i):
		j += 1
		print(j, end = " ")
	print()
