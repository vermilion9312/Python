'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        숫자8은 플레이어 위치를 뜻한다.
        숫자0은 플레이어가 움직일 수 있는 위치이다.
        
        order리스트는 플레이어가 움직이게 하는 명령어이다.
        1,2,3,4는 차례대로 북, 동, 남, 서를 뜻한다. 

        order의 이동대로 플레이어를 이동시키고 출력하시오.
        플레이어가 벽에 붙어서,
        더 이상 원하는 방향으로 이동할 수 없을 때는 "이동 불가"를 출력한다.
    [정답]        
        캐릭터의 현재 위치 = 2 , 2
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0 

        북
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        8 0 0 0 0

        동
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0
'''

game = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,8,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

order = [1,3,3,3,4,3,3,4,2]

#  1,2,3,4는 차례대로 북, 동, 남, 서


print('===[2023-02-10 (화) #02]===')

player = [2, 2]

for v in order:
    if v == 1:
        print("북")
        player[1] -= 1
        if player[1] < 0:
            player[1] = 0
            print("이동불가")
    if v == 2:
        print("동")
        player[0] += 1
        if player[0] > len(game) - 1:
            player[0] = len(game) - 1
            print("이동불가")
    if v == 3:
        print("남")
        player[1] += 1
        if player[1] > len(game) - 1:
            player[1] = len(game) - 1
            print("이동불가")

    if v == 4:
        print("서")
        player[0] -= 1
        if player[0] < 0:
            player[0] = 0
            print("이동불가")

    game = [[0 for j in range(5)] for i in range(5)]

    x = player[0]
    y = player[1]

    game[y][x] = 8

    for arr in game:
        print(arr)
    print()



# print('===[2023-02-10 (화) #01]===')

# player = {
#     "x": 2,
#     "y": 2
# }

# for v in order:
#     if v == 1:
#         print("북")
#         player["y"] -= 1
#         if player["y"] < 0:
#             player["y"] = 0
#             print("이동불가")
#     if v == 2:
#         print("동")
#         player["x"] += 1
#         if player["x"] > len(game) - 1:
#             player["x"] = len(game) - 1
#             print("이동불가")
#     if v == 3:
#         print("남")
#         player["y"] += 1
#         if player["y"] > len(game) - 1:
#             player["y"] = len(game) - 1
#             print("이동불가")
#     if v == 4:
#         print("서")
#         player["x"] -= 1
#         if player["x"] < 0:
#             player["x"] = 0
#             print("이동불가")

#     game = [[0 for j in range(5)] for i in range(5)]

#     x = player["x"]
#     y = player["y"]

#     game[y][x] = 8

#     for arr in game:
#         print(arr)
#     print()







        


