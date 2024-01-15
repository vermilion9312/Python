'''
	[문제]
	  	745의 약수 중에서 작은 수부터 출력했을 때, 
		세 번째 약수만 출력하시오.
	[정답]
		149
'''

print("===[2023-09-21 (목)]===")

num = 1
count = 0

while True:
    
	if 745 % num == 0:
		count += 1

		if count == 3:
			print(num)
			break

	num += 1