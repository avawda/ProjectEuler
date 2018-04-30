import datetime
import os
import Eutils as et

# PROBLEM STATEMENT
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


print("***********")
print(os.path.basename(__file__))
print("***********")
answer = 2
start = datetime.datetime.now()

print("Started process : {}".format(start))
# Custom Problem code starts here

upperBond = 2000000
for i in range(3, upperBond+1, 2):
	if (i+1) % 50000 == 0:
		print(i)
	if et.isPrime(i):
		answer += i

# Custom Problem code starts here
end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
