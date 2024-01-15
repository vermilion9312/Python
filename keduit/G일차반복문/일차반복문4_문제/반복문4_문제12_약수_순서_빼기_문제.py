'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''

print("===[2023-09-21 (목)]===")

num = 1
count = 0

while True:
    
	if 100 % num == 0:
		count += 1

		if count == 2:
			answer = -num
		if count == 5:
			answer += num
			break

	num += 1

print(answer)