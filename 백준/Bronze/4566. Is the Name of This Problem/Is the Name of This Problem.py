sentence = list(input())
while ''.join(sentence) != "END":
	flag = False
	sec_flag = False
	string = ''
	check_string = ''
	quotes_count = 0
	for i in range(len(sentence)):
		if i == 0:
			if sentence[i] != '''"''':
				flag = True
				break
			else:
				quotes_count += 1
				flag = True
				continue
		if flag:
			if sentence[i] == '''"''':
				flag = False
				sec_flag = True
				quotes_count += 1
				continue
			else:
				string += sentence[i]
		if sec_flag:
			check_string += sentence[i]
	try:
		if not flag and check_string[0] == ' ' and check_string[1:] == string and quotes_count == 2 and check_string and string:
			for i in string:
				if i != ' ':
					flag = True
					break
			if flag:
				print(f'Quine({string})')
			else:
				print('not a quine')
		else:
			print('not a quine')
	except IndexError:
		print('not a quine')
	sentence = list(input())