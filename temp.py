n = int(input())
balloon = list(map(int, input().split()))
arrow = [False for _ in range(n + 2)]

firstBalloonHeight = balloon[0]
arrow[firstBalloonHeight] = True

for i in range(n - 1):

	balloonHeight = balloon[i]
	arrow[balloonHeight] = True

	if balloonHeight - 1 == balloon[i + 1]:
		arrow[balloonHeight] = False
		arrow[balloonHeight - 1] = True
	else:
		arrow[balloonHeight] = True
		
print(arrow.count(True))