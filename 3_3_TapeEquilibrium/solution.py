'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]

    list_len = len(A)
    # sum from the left
    left_sum = []
    sum_value = 0
    for i in range(list_len-1):
        sum_value += A[i]
        left_sum.append(sum_value)
    #print(left_sum)
    # sum from the right
    right_sum = []
    sum_value = 0
    for i in range(list_len-1, 0, -1):
        sum_value += A[i]
        right_sum.append(sum_value)
    #print(right_sum)

    # calculate diff
    div_count = len(A) - 1
    min_diff = 99999999
    for i in range(div_count):
        abs_diff = abs(left_sum[i] - right_sum[div_count-i-1])
        if abs_diff < min_diff:
            min_diff = abs_diff
    # print(min_diff)

    return min_diff
    pass

print(solution([3, 1, 2, 4, 3]))
print(solution([3]))
print(solution([]))
print(solution([1, 2001]))