'''
    [문제]
        a 와 b 를 각각 비교해서 더 큰 값을 출력한다. 
        서로 같으면 둘 다 출력한다.
    [정답]
        54
        43
        23
        12 12
        53
'''

a = [10,43,23,12,53]
b = [54,6,4,12,50]

print('===[2023-09-23(토)]===')

for i in range(len(a)):
    if a[i] > b[i]:
        print(a[i])
    elif a[i] < b[i]:
        print(b[i])
    else:
        print(a[i], b[i])