'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때, 
        백의 자리가 3인 두 번째 약수를 출력하시오.
	[정답]
		396
'''

print("===[2023-09-21 (목)]===")

num = 1
count = 0

while True:
    
	if 1980 % num == 0 and num // 100 == 3:
		count += 1

		if count == 2:
			print(num)
			break

	num += 1