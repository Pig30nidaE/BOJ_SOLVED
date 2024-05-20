from string import ascii_lowercase

l = int(input())
string = input()
alpha = ascii_lowercase

al_dict = dict()
num = 1
for i in alpha:
	al_dict[i] = num
	num += 1
k = 0
for i in range(1, len(string) + 1):
	k += al_dict[string[i - 1]] * pow(31, i - 1)
print(k)