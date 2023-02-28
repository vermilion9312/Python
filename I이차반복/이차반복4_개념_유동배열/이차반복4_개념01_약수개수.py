'''
	[문제]
		a리스트의 각 값의 약수를 전부 출력하고 
		각 약수의 개수를 count리스트에 추가하시오.

	[예시]
		1 43 
		1 5 11 55 
		1 5 13 65 
		1 11 		
		count = [2, 4, 4, 2]
	
	[정답]
		count = [2, 4, 4, 2]
'''
a = [43,55,65,11]
count = []
print('===[2023-02-04 (토)]===')


for v in a:
	cnt = 0
	for i in range(1, v + 1):
		if v % i == 0:
			cnt += 1
			print(i, end = " ")
	count.append(cnt)
	print()
print("count =", count)
















# print('===[정답풀이]===')
# for i in range(len(a)):

# 	val = 0
# 	for j in range(a[i]):
# 		if a[i] % (j + 1) == 0:
# 			print(j + 1, end=" ")
# 			val += 1
# 	print()

# 	count.append(val)

# print(count)
