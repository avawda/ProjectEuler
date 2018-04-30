import time
import os
import Eutils as et

start = time.time()

# Custom Problem code starts here

# Setup ideal results set
outcome = []
for i in range(20,1,-1):
	outcome.append(i)

print(outcome)
goalFound = False
num = 10

while not goalFound:
	factors = []
	for i in outcome:
		if num % i != 0:
			break
		factors.append(i)
	if factors == outcome:
		goalFound = True
	else:
		num+=1

# Custom Problem code starts here
answer = num
end = time.time()
timeTaken = end - start

print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
