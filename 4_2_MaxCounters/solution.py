'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(N, A):
    # write your code in Python 3.6
    # 아래와 같이 하면, 88% 만족, 복잡도는 O(N + M)
    # extreme_large 에 대해서만 TIMEOUT_ERROR 가 발생했다.
    # all max_counter operations     Killed. Hard limit reached: 7.000 sec.    튜닝해야 한다.
    '''
    target_list = [0] * N
    local_maximum = 0
    for x in A:
        if x == N + 1:
            target_list = [local_maximum] * N
            continue
        target_list[x - 1] += 1
        if target_list[x - 1] > local_maximum:
            local_maximum = target_list[x - 1]
    return target_list
    '''

    pass

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))   # [3, 2, 2, 4, 2]
print(solution(5, [3, 4, 4, 6, 1, 4, 4, 6, 1]))   #
