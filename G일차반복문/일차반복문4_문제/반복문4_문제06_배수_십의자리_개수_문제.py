'''
	[문제] 
	   	1000보다 큰 수중에서 8의 배수를 검색하고, 
     	십의자리가 5인 배수를
		가장 작은 수부터 차례대로 4개를 출력하시오.
	[정답]
		1056 1152 1256 1352 
'''
print("===[2023-09-21 (목)]===")

num = 1000
count = 0

while True:
	if num % 8 == 0 and num % 100 // 10 == 5:
		print(num, end=" ")
		count += 1

	if count == 4:
		break

	num += 1