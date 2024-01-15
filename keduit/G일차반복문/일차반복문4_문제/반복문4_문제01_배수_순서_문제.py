'''
	[문제] 
		[1] 100 이상의 숫자 중에서  
			7의 배수를 순차적으로 검색하고,
		[2] 그중 3번째 7의 배수를 출력하시오.
	[정답] 
		119
'''


print("===[2023-01-30 (월)]===")

i = 100
count = 0

while True:
	if i % 7 == 0:
		count += 1
		if count == 3:
			print(i)
	i += 1


# print("===[정답풀이]===")
# count = 0

# i = 100
# while True:
# 	if i % 7 == 0:
# 		count += 1
# 	if count == 3:
# 		print(i)
# 		break
# 	i += 1