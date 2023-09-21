'''
	[문제]
		선호네 반 학생 25명이 체험학습을 가기 위해
		버스를 탔는데, 총 요금이 19400원이었다.

		교통카드를 사용하면 720원이고, 
		현금으로 지불하면 1000원일 때, 

		교통카드를 사용한 학생 수와 현금을 사용한 학생 수는 
		각각 얼마인지 구하시오.
	[정답]
		카드 = 20
		현금 = 5
'''

print("===[2023-09-21 (목)]===")

students = 25
totalFares = 19400
cardFares = 720
cashFares = 1000

x = 1
y = students - x

while True:
    
	if x * cardFares + y * cashFares == totalFares:
		break

	cardStudentCount += 1

print("카드 =", cardStudentCount)
print("현금 =", cashStudentCount)