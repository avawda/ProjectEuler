import time
import os
import Eutils as et
import datetime

start = time.time()

# Custom Problem code starts here
print("Started process : {}".format(datetime.datetime.now()))
primePosFound = False
primePosition = 10001
num = 1
loc = 1
while not primePosFound:
	num += 2
	if et.isPrime(num):
		loc += 1
	if loc == primePosition:
		primePosFound = True

answer = num
# Custom Problem code starts here

print("Ended process : {}".format(datetime.datetime.now()))
end = time.time()
timeTaken = end - start

print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# C:\Python\Anaconda3\python.exe "C:/Users/Ahmed/OneDrive/Data Science/Python/ProjectEuler/Problem7.py"
# Started process : 2017-10-22 19:10:27.890268
# Ended process : 2017-10-22 19:10:28.728463
# Problem7.py
# Answer = 104743
# Time taken = 0.8381950855255127
#
# Process finished with exit code 0

