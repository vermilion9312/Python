'''
	[문제]
	  	120의 약수 중에서 순서대로 약수를 출력했을 때, 
        일의자리가 4인 두 번째 약수를 출력하시오.
	[정답]
		24
'''

print("===[2023-09-21 (목)]===")

num = 1
count = 0

while True:
    
	if 120 % num == 0 and num % 10 == 4:
		count += 1

		if count == 2:
			print(num)
			break

	num += 1