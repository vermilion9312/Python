'''
	[문제]
		아래와 같은 휴대요금제가 있다 .
		B를 선택할 경우 A보다 더 경제적으로 되려면,
		통화 시간을 얼마까지 사용해야 할지 정답을 초로 구하시오.
		A요금제 기본요금 17500원 초당 5원이고, 
		B요금제 기본요금 31000원 초당 2원이다.
	[정답]
		4501
'''

print("===[2023-09-22 (금)]===")

A_PLAN = 17500
B_PLAN = 31000

seconds = 0

while True:

	if B_PLAN + 2 * seconds < A_PLAN + 5 * seconds:
		break
    
	seconds += 1

print(seconds)