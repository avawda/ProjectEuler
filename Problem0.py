import datetime
import os
import Eutils as et

# PROBLEM STATEMENT
#


print("***********")
print(os.path.basename(__file__))
print("***********")
answer = 0
start = datetime.datetime.now()

print("Started process : {}".format(start))
# Custom Problem code starts here

# Custom Problem code starts here
end = datetime.datetime.now()
print("Ended process : {}".format(end))
timeTaken = end - start


print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))
