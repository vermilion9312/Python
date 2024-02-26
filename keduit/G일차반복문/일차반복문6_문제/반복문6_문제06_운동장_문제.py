'''
	[문제]
		철수는 자전거로 운동장 한 바퀴 도는데 70초, 
		민수는 90초가 걸린다. 
		30분 동안 운동장을 돌면 출발점에서 
		다시 만나는 횟수가 몇 번인지 구하시오.
		단, 30분 동안 항상 일정한 속도를 유지한다. 
	[정답]
		2
'''

print("===[2024-02-26 (월)]===")

CS_RUNNING_TIME = 70
MS_RUNNING_TIME = 90
RUNNING_TIME = 30 * 60

encounterCount = 0


seconds = 1
while seconds <= RUNNING_TIME:
    
	if seconds % CS_RUNNING_TIME == 0 and seconds % MS_RUNNING_TIME == 0:
		print(seconds, end=" ")
		encounterCount += 1

	seconds += 1

print(encounterCount)