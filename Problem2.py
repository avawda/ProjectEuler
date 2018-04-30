import time
import os
import Eutils as et

answer = 0
start = time.time()

# Custom Problem code starts here
endReached = False
fib1, fib2 = 1, 2
total = fib2

while (not(endReached)):
    if fib2 < 4000000:
        temp = fib2
        fib2 += fib1
        fib1 = temp
        if et.isEven(fib2):
            total += fib2
    else:
        endReached = True

# Custom Problem code starts here

end = time.time()
timeTaken = end - start

answer = total
print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# Problem2.py
# Answer = 4613732
# Time taken = 0.0
# [Finished in 0.23s]
