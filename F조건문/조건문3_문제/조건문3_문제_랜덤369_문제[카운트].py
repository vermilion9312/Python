'''
[문제]
	[1] 1~99 사이의 랜덤 숫자를 저장한다.
	
	랜덤 숫자 중에서 3이나 6이나 9의 개수가
	[2-1] 2개이면, 짝짝을 출력한다.
	[2-2] 1개이면, 짝을 출력한다.
	[2-3] 0개이면, 해당 숫자를 출력하시오.
	
	[예]
		33	==> 짝짝
		16	==> 짝
		 7	==> 7
'''
print("===[2023-01-17(화) # 02]===")
import random
num = random.randint(1, 99)
num = str(num)

count = 0
for v in num:
	v = int(v)
	if v % 3 == 0 and v != 0:
		count += 1

num = int(num)
if count == 2:
	print(num, "==> 짝짝")
if count == 1:
	print(num, "==> 짝")
if count == 0:
	print(num, "==>", num)



print("===[2023-01-17(화) # 01]===")
import random

num = random.randint(1, 99)

count = 0
tens = num // 10
units = num % 10
if tens == 3 or tens == 6 or tens == 9:
	count += 1
if units == 3 or units == 6 or units == 9:
	count += 1

if count == 2:
	print(num, "==> 짝짝")
if count == 1:
	print(num, "==> 짝")
if count == 0:
	print(num, "==>", num)



print("===[2022-10-28(금) # 01]===")
import random

num = random.randint(1, 99)

십 = num // 10
일 = num % 10

십3배수 = 십 % 3 == 0 and 십 != 0
일3배수 = 일 % 3 == 0 and 일 != 0

if 십3배수 and 일3배수:
	print(num, "==> 짝짝")
if 십3배수 and (not 일3배수):
	print(num, "==> 짝")
if (not 십3배수) and 일3배수:
	print(num, "==> 짝")
if (not 십3배수) and (not 일3배수):
	print(num, "==>", num)

if 십 % 3 == 0 and 십 != 0 and 일 % 3 == 0 and 일 != 0:
	print(num, "==> 짝짝")
if (십 % 3 == 0 and 십 != 0) or (일 % 3 == 0 and 일 != 0):
	print(num, "==> 짝")
if 십 % 3 != 0 and 일 %3 != 0:
	print(num, "==>", num)