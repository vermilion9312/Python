'''
	[문제]
        80의 약수 중에서 순서대로 약수를 출력했을 때, 
        [조건1] 일의자리가 4인 약수들만 출력하고,
        [조건2] 그 전체 합을 출력하시오.
        [조건3] 위 수의 개수도 출력하시오.
    [정답]
        4 
        total = 4
        count = 1    
'''

print('===[2023-01-21 (목) #01]===')

num = 80
total = 0
count = 0

i = 1
while i <= num:
    if num % i == 0 and i % 10 // 1 == 4:
        print(i)
        total += i
        count += 1
    i += 1

print("total =", total)
print("count =", count)