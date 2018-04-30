import datetime
import os
import Eutils as et
import math

# PROBLEM STATEMENT
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

print("***********")
print(os.path.basename(__file__))
print("***********")

start = datetime.datetime.now()

print("Started process : {}".format(start))
# Custom Problem code starts here

pySum = 1000
answerFound = False

for x in range(1, pySum):
	if answerFound:
		break
	for y in range(1, pySum):
		if answerFound:
			break
		zSqrd = x**2 + y**2
		z = math.sqrt(zSqrd)
		sumElements = x + y + int(z)
		if (round(z, 0)**2 == zSqrd) and (x < y < z) and (sumElements == pySum):
			print("{} + {} + {} = ".format(x, y, int(z)), sumElements)
			answer = x*y*int(z)
			answerFound = True

# Custom Problem code starts here

end = datetime.datetime.now()
print("Started process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# C:\Python\Anaconda3\python.exe "C:/Users/Ahmed/OneDrive/Data Science/Python/ProjectEuler/Problem9.py"
# ***********
# Problem9.py
# ***********
# Started process : 2017-10-22 21:22:42.014396
# 200 + 375 + 425 =  1000
# Started process : 2017-10-22 21:22:42.686305
# Answer = 31875000
# Time taken = 0:00:00.671909
#
# Process finished with exit code 0
