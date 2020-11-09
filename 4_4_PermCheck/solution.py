'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6
    list_len = len(A)
    if list_len == 0:
        return 0

    sorted_A = sorted(A)
    if sorted_A[0] != 1:
        return 0

    is_missing = False
    for i in range(list_len-1):
        if sorted_A[i] + 1 == sorted_A[i+1]:
            pass
        else:
            is_missing = True
            break

    return 1 if is_missing is False else 0
    pass

print(solution([4, 1, 3, 2]))       # 1
print(solution([4, 1, 3]))          # 0
print(solution([1, 2, 3]))          # 1
print(solution([1, 55]))            # 0
