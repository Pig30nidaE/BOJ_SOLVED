import datetime

h, m = map(int, input().split())
dt = datetime.datetime(1000, 1, 1, h, m, 0) - datetime.timedelta(minutes=45)
string = dt.strftime("%H %M")
if string[0] == '0':
	string = string[1:]
	if string[2] == '0':
		string = string[:2] + string[3:]
else:
	if string[3] == '0':
		string = string[:3] + string[4:]
print(string)