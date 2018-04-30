import time
import os
import Eutils as et

answer = 0
start = time.time()

# Custom Problem code starts here

palindromes = []
for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        answer = i * j
        if et.isPalindrome(answer):
            palindromes.append(answer)

# Custom Problem code starts here
answer = max(palindromes)

end = time.time()
timeTaken = end - start

print(os.path.basename(__file__))
print("Answer = {}".format(answer))
print("Time taken = {}".format(timeTaken))

# Problem4.py
# Answer = 906609
# Time taken = 1.4349479675292969
# [Finished in 1.554s]
