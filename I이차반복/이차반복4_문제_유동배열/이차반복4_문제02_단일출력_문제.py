'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		
'''
a = [1,1,2,2,3,3,4,100,3]


print('===[2023-02-07 (화) #03]===')
a = [1,1,2,2,3,3,4,100,3]
b = []

for i in range(len(a)):

	check = True
	for j in range(len(b)):
		if a[i] == b[j]:
			check = False
	
	if check:
		b.append(a[i])
print(b)



print('===[2023-02-07 (화) #02]===')
a = [1,1,2,2,3,3,4,100,3]
b = []
for v in a:
	check = True
	if v in b:
		check = False
	
	if check:
		b.append(v)
print(b)



print('===[2023-02-07 (화) #01]===')
a = [1,1,2,2,3,3,4,100,3]

a = set(a)
a = list(a)
a.sort()
print(a)

