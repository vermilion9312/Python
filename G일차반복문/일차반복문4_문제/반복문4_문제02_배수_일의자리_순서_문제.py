'''
	[문제] 
		9의 배수 중 일의 자리가 6인 
		첫 번째 배수를 출력하시오.
	[정답]
 		36
'''

print("===[2023-09-21 (목)]===")

i = 1
while True:
    multiple = 9 * i
    if multiple % 10 == 6:
        print(multiple)
        break
    i += 1
    
print("정답풀이")

i = 1
while True:
    if i % 9 == 0 and i % 10 == 6:
        print(i)
        break
    i += 1