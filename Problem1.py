import time
import os

answer = 0
start = time.time()

# Custom Problem code starts here
total = 0
for num in range(1000):
    if (num % 3 == 0) or (num % 5 == 0):
        total = total + num

end = time.time()
timeTaken = end - start
answer = total
# Custom Problem code ends here

print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# Problem1.py
# Answer = 233168
# Time taken = 0.0
# [Finished in 0.085s]
