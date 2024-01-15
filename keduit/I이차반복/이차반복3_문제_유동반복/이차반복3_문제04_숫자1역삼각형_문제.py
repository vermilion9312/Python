'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		12345
		1234
		123
		12
		1
'''

print('===[2023-01-31 (화)]===')

for i in range(5):
	for j in range(5 - i):
		print(j + 1, end = "")
	print()