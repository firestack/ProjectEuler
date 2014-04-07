#! /usr/bin/env python3
import sys
import threading as t

tArgNum = int( sys.argv[1] )

primes = []
calcsPerSec = 0
number = 0

def isPrime( num ):
	limit = num // 2
	
	if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:return False
	else:
		for i in range(3, limit, 2):
			if num % i == 0:
				return False
		return True

def finder( num ):
	global primes
	global calcsPerSec
	global number
	number = num//2
	number = int(number)
	for i in range(3, number, 2 ):
		if num % i == 0:
			primes.append(i)
			primes.append(num//i)
			if len(primes) > 3 :
				primes.pop(-3)
			return
		calcsPerSec += 1

def threadHeader( num ):
	global primes
	if isPrime(num):
		print("already prime...")
		return 0
	finder(num)
	while not isPrime(primes[-1]):
		finder(primes[-1])

def ThreadFunctions(func,args):
	nT = t.Thread(target=func,args=(args),daemon=True)
	print("Thread created")
	nT.start()
	print("Started Background Thread")
	return nT

def intro():
	print("Build 0.2")
	print("Your Calculation has been started...")
	print("Currently finding the largest prime number of {}".format(tArgNum))
	print("Starting at {}".format(number))

def formatOutput(data):
	if len(data) > 0:
		pass
intro()
threadCalcD = ThreadFunctions(threadHeader,(tArgNum,))

while threadCalcD.isAlive():
	print("working")
	threadCalcD.join(timeout=10)
	print(primes)
else:
	print("finished")

try:
	threadCalcD.join()
except:
	pass


print(primes)

