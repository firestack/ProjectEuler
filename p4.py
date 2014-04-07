import sys
import threading as t

def calc():
	k = 0
	for i in range(990,1001):
		k += i**i
		print(i)
	return k

print(calc())


