'''
	[문제]
		자동차 모형 28개와 로봇 모형 42개를 여러 상자에 나눠 담으려 한다. 
		각 상자마다 자동차 모형 개수와 로봇 모형 개수가 같아야 하며, 
		최대한 많은 상자에 나눠 담을 때 
		자동차 모형 몇 개와 로봇 모형 몇 개씩 넣어야 하는지 구하시오. 
	[정답]
		자동차 = 2
		로봇 = 3
'''

print("===[2023-10-27 (금)]===")

CAR = 28
ROBOT = 42

box = 1

while box <= CAR:
    
	if CAR % box == 0 and ROBOT % box == 0:
		modBox = box

	box += 1

print("자동차 =", CAR // modBox)
print("로봇 =", ROBOT // modBox)