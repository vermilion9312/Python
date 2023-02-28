'''
	[문제]
		a리스트의 값 중 b리스트의 값과 같은 값이 있으면
		total에 저장한다. 
	[정답]
		total = [20, 30]
'''

a = [10, 20, 30, 60]
b = [40, 30, 20, 50]
total = []

print('===[2023-02-07 (화) #03]===')
for i in range(len(a)):
	for j in range(len(a)):
		if a[i] == b[j]:
			total.append(a[i])
print(total)


print('===[2023-02-07 (화) #02]===')
a = [10, 20, 30, 60]
b = [40, 30, 20, 50]
total = []

for v in a:
	if v in b:
		total.append(v)
print(total)


print('===[2023-02-07 (화) #01]===')
a = [10, 20, 30, 60]
b = [40, 30, 20, 50]
total = []

a = set(a)
b = set(b)
total = list(a & b)
print(total)