'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
import random

bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


print('===[2023-02-10 (화) #02]===')


while True:

    row = random.randint(0, len(bingo) - 1)
    col = random.randint(0, len(bingo) - 1)

    if bingo[row][col] == 1:
        continue
    else:
        bingo[row][col] = 1

    print("Pos:", row, col)
    for v in bingo:
        print(v)

    count = 0
    for i in range(len(bingo)):
        if bingo[i][0] == 1 and bingo[i][1] == 1 and bingo[i][2] == 1:
            count += 1
        if bingo[0][i] == 1 and bingo[1][i] == 1 and bingo[2][i] == 1:
            count += 1
    if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
        count += 1
    if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
        count += 1
    
    print("빙고:", count)
    print()

    if count == 3:
        break






# print('===[2023-02-10 (화) #01]===')

# while True:

#     for i in range(len(bingo)):
#         for j in range(len(bingo[i])):
#             r = random.randint(0, 1)
#             bingo[i][j] = r

#     count = 0
#     for i in range(len(bingo)):
#         if bingo[i][0] == 1 and bingo[i][1] == 1 and bingo[i][2] == 1:
#             count += 1
#         if bingo[0][i] == 1 and bingo[1][i] == 1 and bingo[2][i] == 1:
#             count += 1

#     if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
#         count += 1
#     if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
#         count += 1

#     if count == 3:
#         break

# for v in bingo:
#     print(v)
# print("빙고: ", count)




