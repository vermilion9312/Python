# def game(user, oppnent):

#     userScore = 0

#     if user == 'R':
#         if oppnent == 'R':
#             userScore += 1
#         elif oppnent == 'S':
#             userScore += 2
#     if user == 'P':
#         if oppnent == 'P':
#             userScore += 1
#         elif oppnent == 'R':
#             userScore += 2
#     if user == 'S':
#         if oppnent == 'S':
#             userScore += 1
#         elif oppnent == 'P':
#             userScore += 2

#     return userScore
    
# r = int(input())
# user = input()
# n = int(input())

# userScore = 0
# maxUserScore = 0

# for _ in range(n):

#     oppnent = input()
#     count = {'R': 0, 'P': 0, 'S':0}

#     for i in range(r):
#         userScore += game(user[i], oppnent[i])
#         if oppnent[i] == 'R':
#             count['R'] += 1
#         elif oppnent[i] == 'P':
#             count['P'] += 1
#         else:
#             count['S'] += 1

    


# print(userScore)
# print(maxUserScore)

var = 1
var ^= 1
print(var)