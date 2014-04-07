#! /usr/bin/env python3
import threading as t

arr = [i*2+1 for i in range(1,100000)]
primes = [2]

pos = 0
dVal = 0
def primesThread():
	global primes
	global arr
	global pos
	global dVal
	while  len(primes) < 10001:
		dVal = arr[pos]
		rm = []
		for tVal in range(pos+1,len(arr)):
			testValue = arr[tVal] % dVal
			if testValue == 0:
				rm.append(arr[tVal])	
		
		for i in rm:
			arr.remove(i)
		rm.clear()
		primes.append(dVal);pos += 1
	print(len(primes))

calcd = t.Thread(target=primesThread)
calcd.daemon = True
calcd.start()
mpos = 0
while calcd.isAlive():
	if mpos != dVal:
		print("finished with {} moving to {}".format(mpos,dVal))
		mpos = dVal 
	calcd.join(timeout=1)
	

print(primes[-1])
fout = open("primes.txt","w")
for p in primes:
	fout.write("{}\n".format(p))
fout.close()
