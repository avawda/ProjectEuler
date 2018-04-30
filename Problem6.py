import time
import os
import Eutils as et

answer = 0
start = time.time()


# Custom Problem code starts here
max = 100
sumOfSqr = 0
sqrOfSum = 0

for i in range(1,max+1):
	sumOfSqr+=i
	sqrOfSum = sqrOfSum + (i * i)

sumOfSqr = sumOfSqr * sumOfSqr
# Custom Problem code starts here
print("Upper Bound  = {}".format(max))
print("Sum          = {}".format(sumOfSqr))
print("Squares      = {}".format(sqrOfSum))

answer = sumOfSqr - sqrOfSum
end = time.time()
timeTaken = end - start

print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
