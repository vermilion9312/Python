'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''

print("===[2023-09-21 (목)]===")

num = 1

while True:
	if 200 % num == 0 and num % 2 == 0:
		if num <= 80:
			underOrEqual = num
		else:
			over = num
			break
	num += 1

if 80 - underOrEqual < over - 80:
	print(underOrEqual)
else:
	print(over)