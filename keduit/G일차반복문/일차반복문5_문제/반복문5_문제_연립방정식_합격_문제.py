'''
	[문제]
		철수는 두 번의 시험에서 각각 80점과 72점을 받았다.
		세 번째 시험에서 최소 몇 점 이상을 받아야 
		
		세 번의 시험성적의 평균이 82점 이상이 될 수 있을까?
		시험점수는 1점 단위로 설정된다.
	[정답]
		94
'''

print("===[2023-09-22 (금)]===")

import math

FIRST_SCORE = 80
SECOND_SCORE = 72
SCORE_AVG = 82

thirdScore = 0

while True:

	if (FIRST_SCORE + SECOND_SCORE + thirdScore) / 3 >= SCORE_AVG:
		break
    
	thirdScore += 1

print(thirdScore)