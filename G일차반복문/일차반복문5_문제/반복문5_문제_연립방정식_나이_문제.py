'''
	[문제]
		철수는 13살 철수의 아버지는 45살이다. 
		몇 년 후 철수의 아버지는 철수 나이의 3배가 될지 구하시오.
	[정답]
		3
'''

print("===[2023-09-22 (금)]===")

myAge = 13
fatherAge = 45
yearCount = 0

while True:
	
	yearCount += 1

	if 3 * (myAge + yearCount) == fatherAge + yearCount:
		break
    
print(yearCount)