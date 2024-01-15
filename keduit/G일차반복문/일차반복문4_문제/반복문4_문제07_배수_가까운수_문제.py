'''
	[문제] 
  		6의 배수를 순차적으로 검사한다. 
  		그중 100에 가장 가까운 수를 출력하시오. 
 	[정답]
		102
'''

print("===[2023-09-21 (목)]===")

num = 1

while True:
	if num % 6 == 0:
		if num < 100:
			underNum = num
		elif num > 100:
			overNum = num
			break
	num += 1

if 100 - underNum < overNum - 100:
	print(underNum)
else:
	print(overNum)