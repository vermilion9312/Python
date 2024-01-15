'''
	[문제]
        철수는 게임을 만들고 있다. 
        (1~6 사이의 랜덤 숫자)주사위를 던져
		해당 숫자만큼 캐릭터를 이동시킨다.
		단, 캐릭터는 외곽으로만 움직일 수 있다.
		두 바퀴를 돌고 게임을 끝내시오.
	[예시]
		옷 □ □ □ □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 2   
		□ □ □ 옷 □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ 옷 
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ 옷 □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 6
		옷 □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 5
		□ □ □ □ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		옷 ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ 옷 □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

'''
import random

player = {
	"x": 0,
	"y": 0
}

mapSize = 5

map = []
for i in range(mapSize):
	map.append([])
	for j in range(mapSize):
		if i >= 1 and i <= 3 and j >= 1 and j <= 3:
			map[i].append("■")
		else:
			map[i].append("□")

x = player["x"]
y = player["y"]
map[y][x] = "▲"

for i in range(mapSize):
	for j in range(mapSize):
		print(map[i][j], end = " ")
	print()


# while True:
# 	dice = random.randint(1, 6)
# 	print("dice =", dice)

# 	if player["y"] == 0:
# 		player["x"] += dice //