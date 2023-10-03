'''
	[문제] 
		45와 60, 75의 최대공약수를 구하시오.
	[정답]
		15
'''

num = 1

while True:

	if 45 % num == 0 and 60 % num == 0 and 75 % num == 0:
		print(num)
		break

	num += 1