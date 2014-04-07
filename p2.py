def genNew(myInt):
	start = 1
	arr = [1,2]
	log = [1,2]
	for i in range(int(myInt)):
		newSum = sum(log)
		log[0] = log[1]
		log[1] = newSum		
		arr.append(newSum)

	return arr
def getEven(arr):
	newArr = []
	for i in arr:
		if i%2 == 0 and i<4000000:
			newArr.append(i)
	return newArr

def paste(arr):
	fout = open('test','w')
	size = len(arr)
	rate = size//100
	for i,k in zip(arr,range(len(arr))):
		fout.write('%d\n'%i)
		if k%rate== 0:
			print((k/rate),'%')
print('build 0.1')
print('Lowest number allowed is 1000')
toNew = input('please enter amount list elements to create\n:>>')
toNew = int(toNew)
if toNew < 1000:
	toNew = 1000
fNumArr = genNew(toNew)
print(sum(getEven(fNumArr)))
paste(fNumArr)
