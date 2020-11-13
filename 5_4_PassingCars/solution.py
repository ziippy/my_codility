'''
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6
    # 이렇게 짜니 100% 만족. 복잡도는 O(N) 이었다. 한방에 성공~
    total_passing_cars = 0
    tmp_car_count = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 1:
            tmp_car_count += 1
        else:
            total_passing_cars += tmp_car_count

        if total_passing_cars > 1000000000:
            return -1

    return total_passing_cars
    pass

print(solution([0, 1, 0, 1, 1]))              # 5
print(solution([1, 1, 0, 1, 1]))              # 5

def do_random_test():
    # N 은 1~100000
    # 배열 A 의 각 요소는 0 or 1

    import random
    n_value = 10000
    target_list = []
    for i in range(n_value):
        random_num = random.randint(0, 1)
        target_list.append(random_num)
    # print(p_list)
    # print(q_list)

    #random_str = 'CAGCCTA'

    import time
    a = time.time()
    print(solution(target_list))
    b = time.time()
    print('Elapsed: ', b - a)

do_random_test()
