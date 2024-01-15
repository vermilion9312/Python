'''
	[문제] 
		45와 60, 75의 최대공약수를 구하시오.
	[정답]
		15
'''

print("===[2023-10-25 (수)]===")

num = 1

while num <= 45:

	if 45 % num == 0 and 60 % num == 0 and 75 % num == 0:
		result = num

	num += 1

print(result)