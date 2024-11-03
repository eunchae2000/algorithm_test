from functools import reduce
from math import gcd

def gcd_num(arr):
    return reduce(gcd, arr)

def check(current, other_arr):
    for num in other_arr:
        if num % current == 0:
            return False
    return True

def solution(arrayA, arrayB):
    gcdA = gcd_num(arrayA)
    gcdB = gcd_num(arrayB)
    
    resultA = gcdA if check(gcdA, arrayB) else 0
    resultB = gcdB if check(gcdB, arrayA) else 0
    
    return max(resultA, resultB)