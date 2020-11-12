'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6

    # 아래와 같이 짜면 60% 만족, 복잡도는 O(N ** 2), TIMEOUT_ERROR 발생
    '''
    # 0번째부터 쭈욱 더 한 값이 있는 array 생성
    import time
    a = time.time()
    sum_list = []
    sum_value = 0
    for x in A:
        sum_value += x
        sum_list.append(sum_value)
    # print(sum_list)
    b = time.time()
    print('Create sum array elapsed: ', b - a)

    min_slice_average = 9999999
    min_slice_start_pos = -1

    list_len = len(A)
    for i in range(0, list_len, 1):
        for j in range(i+1, list_len, 1):
            slice_count = (j - i) + 1
            #
            slice_start = i - 1
            slice_end = j
            #
            end_value = sum_list[slice_end]
            start_value = sum_list[slice_start] if slice_start >= 0 else 0
            #
            slice_average = (end_value - start_value) / (slice_count)
            # if slice_average == 0:
            #     return i
            # print(f'{i} ~ {j} : {slice_average}')
            if slice_average < min_slice_average:
                min_slice_average = slice_average
                min_slice_start_pos = i

    return min_slice_start_pos
    '''

    # 다르게 짜자
    # 슬라이스 한 평균의 최소값은 반드시 크기가 2나 3인 슬라이스라는 수학적 지식이 필요하단다..
    # a < b < c < d 일 때 a < (a+b)/2 < b 그리고 c < (c+d)/2 < d 이고 (a+b)/2 < (c+d)/2 이니까
    # 결과적으로 (a+b)/2 < (a+b+c+d)/4 < (c+d)/2 임..
    # 이렇게 짜니 100% 만족. 복잡도는 O(N) 이었다.
    #
    # 0번째부터 쭈욱 더 한 값이 있는 array 생성
    # import time
    # a = time.time()
    sum_list = []
    sum_value = 0
    for x in A:
        sum_value += x
        sum_list.append(sum_value)
    # print(sum_list)
    # b = time.time()
    # print('Create sum array elapsed: ', b - a)

    min_slice_average = 9999999
    min_slice_start_pos = -1

    list_len = len(A)
    for i in range(0, list_len, 1):
        for j in range(i + 1, list_len, 1):
            if j - i > 2:
                break
            slice_count = (j - i) + 1
            #
            slice_start = i - 1
            slice_end = j
            #
            end_value = sum_list[slice_end]
            start_value = sum_list[slice_start] if slice_start >= 0 else 0
            #
            slice_average = (end_value - start_value) / (slice_count)
            print(f'{i} ~ {j} : {slice_average}')
            if slice_average < min_slice_average:
                min_slice_average = slice_average
                min_slice_start_pos = i

    return min_slice_start_pos

    pass

print(solution([4, 2, 2, 5, 1, 5, 8]))              # 1

def do_random_test():
    # N 은 2~100000
    # 배열 A 의 각 요소는 -10000 ~ 10000

    import random
    n_value = 10000
    target_list = []
    for i in range(n_value):
        random_num = random.randint(-10000, 10000)
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
