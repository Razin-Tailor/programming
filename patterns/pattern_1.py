n = int(input("Please enter pyramid depth: "))

for i in range(n+1, 1, -1):
	j_list = list()
	for j in range(0, i):
		j_list.append(j+n)
	print(j_list)



	# for j in range(0, i):
	# 	print(j+n)