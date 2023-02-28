'''
	[달팽이]
		a에 아래와같이 저장후 출력하시오..
	  
	  
	1 	2	3	4	5	
	16	17	18	19	6	
	15	24	25	20	7	
	14	23	22	21	8	
	13	12	11	10	9

	1 	2	3	4	5	
	16	17	18	19	6	
	15	24	25	20	7	
	14	23	22	21	8	
	13	12	11	10	9
'''

a = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],]


i = 0
j = 0
m = 4
op = 1
count = 0
turn = True
for k in range(25):
	k += 1

	if turn == True:
		a[i][j] = k
	if turn == False:
		a[j][i] = k
	if j % 5 == m:
		i, j = j, i
		count += 1
		turn = not turn

		if count == 2:
			op = - op
			m -= 1
			count = 0
	j += op


		


for v in a:
	print(v)
	
