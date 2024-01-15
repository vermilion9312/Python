'''
[문제]
	852의 약수 중에서 큰 수부터 작은 수를 거꾸로 출력했을 때,
	다섯 번째 약수만 출력하시오.
[정답]
	142
'''

print('===[2023-01-23 (월) #01]===')

num = 852
count = 0

i = num
while i >= 1:
	if num % i == 0:
		count += 1
	if count == 5:
		print(i)
		break
	i -= 1

# print("===[정답풀이]===")

# count = 0

# i = 852
# while i >= 1:
# 	if 852 % i == 0:
# 		count += 1

# 		if count == 5:
# 			print(i)

# 	i -= 1

