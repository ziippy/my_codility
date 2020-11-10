'''
Write a function:

class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A, B, K):
    # write your code in Python 3.6


    # 이렇게 짜면 62% 만족, 복잡도는 O((B-A)/K), TIMEOUT_ERROR 가 발생한다.
    '''
    count_sum = 0
    first_divided_num = 0
    first_num_found = False
    for i in range(A, B+1, 1):
        if i % K == 0:
            first_divided_num = i
            first_num_found = True
            break

    if first_num_found is True:
        for i in range(first_divided_num, B+1, K):
            count_sum += 1

    return count_sum
    pass
    '''

    # 이렇게 짜면 100% 만족, 복잡도는 O(1)
    count_sum = 0
    first_divided_num = 0
    first_num_found = False
    for i in range(A, B + 1, 1):
        if i % K == 0:
            first_divided_num = i
            first_num_found = True
            break

    if first_num_found is True:
        count_sum = int((B - first_divided_num) / K) + 1

    return count_sum
    pass

print(solution(10, 10, 5))               # 0
print(solution(6, 11, 2))               # 3
print(solution(6, 8, 9))                # 0
print(solution(10, 10, 11))             # 0
#print(solution(0, 2000000000, 1))       # 2000000001
print(solution(100, 123000000, 2))      # 61499951
