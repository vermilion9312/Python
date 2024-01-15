'''
	[문제]
		a리스트와 b리스트를 비교하여 
		서로 겹치는 값을 0으로 변경하시오.
		겹치는 값이 여러 개면 전부 0으로 변경하시오.
	[정답]
		a = [0, 0, 30, 40, 0]
		b = [0, 3, 0, 0, 0, 50]
'''

a = [10, 20, 30, 40, 20]
b = [10, 3, 20, 10, 20, 50]

print("===[230316-4-1107]===")

for i in range(len(a)):

    isDuplicate = False

    for j in range(len(b)):
        if a[i] != 0 and a[i] == b[j]:
            isDuplicate = True
            b[j] = 0

    if isDuplicate:
        a[i] = 0

print("a =", a)
print("b =", b)


# print("===[정답풀이]====")

# for i in range(len(a)):
# 	check = -1
# 	for j in range(len(b)):
# 		if a[i] == b[j]:
# 			check = a[i]
# 			b[j] = 0

# 	if check != -1:
# 		for j in range(len(a)):
# 			if check == a[j]:
# 				a[j] = 0
# print("a =", a)
# print("b =", b)
