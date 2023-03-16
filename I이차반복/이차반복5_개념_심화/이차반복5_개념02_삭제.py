'''
	[문제]
		a리스트안에는 1~5의 값이 추가되어 있다. 
		랜덤(1~10) 숫자를 10번 발생시켜
		랜덤 값이 a리스트안에 있으면 a리스트에서 삭제하고,
		없으면 "삭제불가" 를 출력한다.
	[예시] 
		r = 9 : 삭제불가
		r = 9 : 삭제불가
		r = 8 : 삭제불가
		r = 3 : [1, 2, 4, 5]
		r = 6 : 삭제불가
		r = 6 : 삭제불가
		r = 8 : 삭제불가
		r = 5 : [1, 2, 4]
		r = 1 : [2, 4]
		r = 6 : 삭제불가
'''
import random

a = [1, 2, 3, 4, 5]

print("===[230316-4-1050]===")

for _ in range(10):

    r = random.randint(1, 10)
    isDuplicate = False

    for i in range(len(a)):
        if r == a[i]:
            isDuplicate = True
            break

    if isDuplicate:
        a.remove(r)
        print("r =", r, ":", a)
    else:
        print("r =", r, ": 삭제불가")


# print("===[정답풀이]===")

# for i in range(10):
#     r = random.randint(1, 10)
#     print("r =", r, end=" : ")

#     check = -1
#     for j in range(len(a)):
#         if r == a[j]:
#             check = j
#             break

#     if check != -1:
#         del a[check]
#         print(a)
#     else:
#         print("삭제불가")
