import sys
from math import sqrt
input = sys.stdin.readline


def getQuad(x: int, y: int)->int:
	if x > 0 and y > 0:
		return 1
	elif x < 0 and y > 0:
		return 2
	elif x > 0 and y < 0:
		return 3
	elif x < 0 and y < 0:
		return 4
	elif x > 0 and y == 0:
		return 11
	elif x < 0 and y == 0:
		return -11
	elif x == 0 and y > 0:
		return 22
	elif x == 0 and y < 0:
		return -22
	else:
		return 0

def getDistance(x: int, y: int)->float:
	return sqrt(x*x + y*y)

n = int(input())
slopeDict = dict()
for _ in range(n):
	x, y = map(int, input().split())
	try:
		slope = y / x
	except ZeroDivisionError:
		slope = "inf"
	quad = getQuad(x, y)
	try:
		if getDistance(x, y) < getDistance(slopeDict[(slope, quad)][0], slopeDict[(slope, quad)][1]):
			slopeDict[slope][0] = x
			slopeDict[slope][1] = y
	except KeyError:
		slopeDict[(slope, quad)] = [x, y]
print(len(slopeDict.keys()))