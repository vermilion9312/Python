'''
	[문제]
		철수가 편의점에서 우유를 15개 구입하려고 한다. 
		한 개에 1000원인 흰 우유와 
		한 개에 1200원인 초코 우유를 합쳐서 총 15개 구입했다.
		20000원을 내고 4200원을 거슬러 받았을 때 
		철수가 구입한 흰 우유는 몇 개인지 구하시오.
	[정답]
		11
'''

print("===[2023-09-22 (금)]===")

PLAIN_MILK_PRICE = 1000
CHOCO_MILK_PRICE = 1200
TOTAL_MILK_COUNT = 15
TOTAL_MILK_PAYMENT = 20000 - 4200

plainMilkCount = 0

while True:
    
	chocoMilkCount = TOTAL_MILK_COUNT - plainMilkCount

	if PLAIN_MILK_PRICE * plainMilkCount + CHOCO_MILK_PRICE * chocoMilkCount == TOTAL_MILK_PAYMENT:
		break

	plainMilkCount += 1

print(plainMilkCount)