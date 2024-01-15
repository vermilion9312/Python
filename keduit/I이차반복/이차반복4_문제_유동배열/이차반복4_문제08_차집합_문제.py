'''
	[문제]
		a와 b 두 리스트를 비교해서 서로 겹치지 않는 값을 
		temp에 저장하고 출력하시오.
	[정답]
		temp = [6, 4, 20, 3, 17, 13, 7]
'''
a = [16,  5, 11, 6, 19, 12, 18,  4, 20, 3]
b = [17, 11, 19, 5, 13, 18, 16, 12, 11, 7]
temp = []

print('===[2023-03-08(수) #03]===')
for i in range(len(a)):

	isDuplicate = False
	for j in range(len(b)):
		if a[i] == b[j]:
			isDuplicate = True
			break

	if isDuplicate == False:
		temp.append(a[i])

for i in range(len(b)):

	isDuplicate = False
	for j in range(len(a)):
		if b[i] == a[j]:
			isDuplicate = True
			break

	if isDuplicate == False:
		temp.append(b[i])

temp.sort()
print(temp)


print('===[2023-03-08(수) #02]===')
temp = []
for v in a:
	if v not in b:
		temp.append(v)

for v in b:
	if v not in a:
		temp.append(v)

temp.sort()
print(temp)


print('===[2023-03-08(수) #01]===')

a = set(a)
b = set(b)

temp = list((a - b) | (b - a))
temp.sort()

print(temp)
