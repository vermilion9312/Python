'''
[문제]
	18의 약수를 출력하고, 전체 합을 구하시오.
[정답]
	1 2 3 6 9 18 
	합 = 39
'''

print('===[2023-01-19(목) #01]===')

total = 0
num = 18

i = 1
while i <= num:
	if num % i == 0:
		print(i, end = " ")
		total += i
	i += 1

print()
print("합 =", total)

# print('===[정답풀이]===')

# num = 18
# total = 0

# i = 1
# while i <= num:
# 	if num % i == 0:
# 		print(i, end=" ")
# 		total += i
# 	i += 1

# print()
# print("total =", total)