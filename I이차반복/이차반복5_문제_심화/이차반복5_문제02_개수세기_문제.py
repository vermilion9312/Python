'''
	[문제]
		a리스트의 값을 중복없이 value에 저장한다.
		그리고 중복되는 개수를 count에 저장한다.
	[정답]
		value = [10,20,30,100]
		count = [2,3,5,1]
'''

a = [10, 20, 30, 30, 100, 10, 30, 30, 20, 30, 20]

value = []
count = []

print("===[230405-3-1412]===")

for i in range(len(a)):
	
	isDuplicate = False
	for j in range(len(value)):
		if a[i] == value[j]:
			isDuplicate = True
			break

	if isDuplicate:
		continue
	else:
		value.append(a[i])

print("value =", value)

for i in range(len(value)):

	cnt = 0
	for j in range(len(a)):
		if value[i] == a[j]:
			cnt += 1

	count.append(cnt)

print("count =", count)