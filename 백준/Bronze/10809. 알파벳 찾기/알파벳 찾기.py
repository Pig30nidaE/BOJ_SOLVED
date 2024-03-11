from string import ascii_lowercase

low_list = list(ascii_lowercase)
string = input()
for i in low_list:
	print(string.find(i), end=" ")
