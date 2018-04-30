import time
import os
import Eutils as et

answer = 0
start = time.time()
inputNum = 600851475143

# Custom Problem code starts here
factors = et.getFactors(inputNum)
primeFactors = []
for num in factors:
    if (et.isPrime(num)):
        primeFactors.append(num)

# Custom Problem code starts here
answer = max(primeFactors)
end = time.time()
timeTaken = end - start

print(os.path.basename(__file__))
print("Input Number     : {}".format(inputNum))
print("Factors          : {}".format(factors))
print("PRIME factors    : {}".format(primeFactors))
print("\n")
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# Problem3.py
# Input Number     : 600851475143
# Factors          : [1, 71, 839, 1471, 6857, 59569, 104441, 486847]
# PRIME factors    : [71, 839, 1471, 6857]
#
#
# Answer = 6857
# Time taken = 0.11807870864868164
# [Finished in 0.256s]
