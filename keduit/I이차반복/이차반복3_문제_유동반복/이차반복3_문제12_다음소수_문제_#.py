'''
	[문제]
		2~1000 사이의 랜덤 숫자 하나를 저장한다.
		위 숫자 바로 다음 소수를 출력하시오.
	
	[예시1]
		r = 1000
		소수 = 1009	 
	[예시2]
		r = 500
	    소수 = 503
'''

print('===[2023-02-04 (토)]===')

import random
r = random.randint(2, 1000)
# r = 1000
# r = 500
print("r =", r)


i = r
while True:
	check = True

	j = 2
	while j * j <= i: 
		if i % j == 0:
			check = False
		j += 1

	if check:
		break
	i += 1
print("소수 =", i)