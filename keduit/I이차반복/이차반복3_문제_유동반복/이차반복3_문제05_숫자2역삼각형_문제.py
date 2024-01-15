'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		123123
		12312
		1231
		123
		12
		1
'''

print('===[2023-01-31 (화)]===')

for i in range(6):
	val = 0
	for j in range(6 - i):
		print(val + 1, end = "")
		val += 1
		if val == 3:
			val = 0
	print()