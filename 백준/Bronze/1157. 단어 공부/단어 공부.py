string = input().upper()
toFind = list(set(string))
num_list = list()
for i in toFind:
	num_list.append((i, string.count(i)))
num_list.sort(key=lambda x:x[1])
if len(num_list) > 1:
	if num_list[-1][1] == num_list[-2][1]:
		print('?')
	else:
		print(num_list[-1][0])
else:
	print(num_list[-1][0])