'''
	[문제] 
		9의 배수 중 십의 자리가 6인 
		다섯 번째 배수를 출력하시오.
	[정답]
		369
'''
print("===[2023-09-21 (목)]===")
i = 1
count = 0
while True:
    if i % 9 == 0 and i % 100 // 10 == 6:
        count += 1
        if count == 5:
            print(i)
            break
    i += 1