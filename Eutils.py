# A set of mathematical tools for us with Project Euler problems
import math


def isEven(p_input):
    if p_input % 2 == 0:
        return True
    return False


def isOdd(p_input):
    if p_input % 2 != 0:
        return True
    return False


def isFactor(p_input, check):
    if p_input % check == 0:
        return True
    return False


def getFactors(p_input):
    factors = []
    for i in range(1, int(math.sqrt(p_input) + 1)):
        if p_input % i == 0:
            factors.append(i)
    return factors


# Previously used method
# def isPrime(p_input):
#     if (isEven(p_input)) or (p_input <= 1):
#         return False
#     if len(getFactors(p_input)) == 1:
#         return True
#     return False


primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def isPrime(p_input):
    if p_input <= 100:
        return p_input in primes_under_100
    if p_input % 2 == 0 or p_input % 3 == 0:
        return False

    for f in range(5, int(p_input ** .5) + 1, 6):  # only check till the square root of the input
        if p_input % f == 0 or p_input % (f + 2) == 0:
            return False
    return True


def isPalindrome(p_input):
    # inStr = str(p_input)
    output = str(p_input)[::-1]
    if str(p_input) == output:
        return True
    return False
