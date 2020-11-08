'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6
    # 시간 복잡도는 O(N) or O(N * log(N))
    # 우선 비어있을 경우 1 리턴
    a_len = len(A)
    if a_len == 0:
        return 1

    sorted_A = sorted(A)
    for i in range(0, a_len, 1):
        if sorted_A[i] != i + 1:
            return i + 1
    return sorted_A[a_len-1] + 1
    pass

print(solution([2, 3, 1, 5]))
print(solution([2]))
print(solution([]))
print(solution([3, 2, 1]))