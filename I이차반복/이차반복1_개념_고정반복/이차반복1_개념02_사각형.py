'''
	[사각형그리기]
		랜덤으로 세로(3~6)을 저장하고, 각 길이에 맞게 사각형을 그려보시오. 
		단 가로는 항상 5이다.
		일차원 반복문과 이차원 반복문으로 그려보시오.
	[예시] 
		세로 : 3
  
		#####
		#####
		#####
'''

print('===[2023-01-28(화)]===')
import random
row = random.randint(3 ,6)
print("세로:", row)

print("===[일차반복문]===")
for _ in range(row):
	print("#####")

print("===[이차반복문]===")
for i in range(row):
	for j in range(5):
		print("#", end = "")
	print()







# print('===[정답풀이]===')
# import random

# sero = random.randint(3, 6)
# print("세로 :", sero)

# print("--------------------")
# for i in range(sero):
#     print("#####")
	
# print("--------------------")
# for i in range(sero):
#     for j in range(5):
#         print("#", end="")
#     print()