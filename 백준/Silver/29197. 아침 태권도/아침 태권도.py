import sys
from math import sqrt, pow
input = sys.stdin.readline



def getDistance(x: int, y: int)->float:
	return sqrt(pow(x, 2) + pow(y, 2))

def isOnTheLine(slope: float, x: int, y: int)->bool:
	if y == slope * x:
		return True
	return False

n = int(input())
slopeDict = dict()
for _ in range(n):
	x, y = map(int, input().split())
	slope = y / x
	try:
		if getDistance(x, y) < getDistance(slopeDict[slope][0], slopeDict[slope][1]):
			slopeDict[slope][0] = x
			slopeDict[slope][1] = y
	except KeyError:
		slopeDict[slope] = [x, y]
print(len(slopeDict.keys()))