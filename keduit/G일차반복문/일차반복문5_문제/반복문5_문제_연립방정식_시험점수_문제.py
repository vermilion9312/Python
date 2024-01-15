'''
	[문제]
		철수네 학교의 수학 시험은 4점짜리 문제와 5점짜리 문제가 섞여서 출제된다.	
		철수는 20개의 문제를 맞혀서 90점을 받았다. 	
		각각 몇 문제씩 맞혔는지 구하시오. 
		주석으로 표현하시오.
	[정답]
		4점 문제 = 10
		5점 문제 = 10
'''

print("===[2023-09-22 (금)]===")

fourPointCount = 0
TOTAL_EXAM_COUNT = 20
TOTAL_EXAM_POINT = 90

while True:
	
	fivePointCount = TOTAL_EXAM_COUNT - fourPointCount
    
	if 4 * fourPointCount + 5 * fivePointCount == TOTAL_EXAM_POINT:
		break

	fourPointCount += 1

print("4점 문제 =", fourPointCount)
print("5점 문제 =", fivePointCount)