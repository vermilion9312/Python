'''
[문제] 
	45와 60, 75의 최소공배수를 구하시오.
[정답]
	900
'''

print("===[2023-10-25 (수)]===")

num = 1

while True:
    
	if num % 45 == 0 and num % 60 == 0 and num % 75 == 0:
		print(num)
		break

	num += 1