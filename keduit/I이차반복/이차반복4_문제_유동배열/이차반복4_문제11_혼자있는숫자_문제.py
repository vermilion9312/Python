'''
	[문제]
		a리스트에서 혼자있는 숫자만 출력하시오.
	[정답]
		20 50
'''

a = [10, 20, 30, 40, 40, 10, 30, 10, 50]

print('===[2023-03-08(수)]===')

for i in range(len(a)):

	isAlone = True
	for j in range(len(a)):
		if i != j and a[i] == a[j]:
			isAlone = False
			break
	
	if isAlone:
		print(a[i], end=" ")