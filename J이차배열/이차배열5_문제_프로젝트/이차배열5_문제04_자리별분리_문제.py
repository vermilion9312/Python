'''
	[문제]
		랜덤으로 10000 ~ 99999 사이의 랜덤숫자를 저장하고 
		다음 규칙에 따라 결과를 출력하시오.
		랜덤숫자를 두 개로 분리하는데
		한 자리씩 늘리면서 분리한다. 
		각 분리한 숫자의 합을 출력한다.
	[예시]
		r = 34567
	[결과]
		3 + 4567
		34 + 567
		345 + 67
		3456 + 7
'''

import random
print('===[2023-02-11 (화)]===')

r = random.randint(10000, 99999)
print("r =", r)

r = str(r)

side1 = ""
side2 = ""
for i in range(len(r) - 1):
    side1 = r[0:i + 1]
    side2 = r[i + 1: len(r)]
    print(side1, "+", side2, "=", int(side1) + int(side2))
