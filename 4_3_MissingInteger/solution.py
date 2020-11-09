'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(A):
    # write your code in Python 3.6
    # 길이가 0 이면 1 리턴
    # 길이가 1 인데, 값이 1 이면 2 리턴
    # 길이가 1 인데, 값이 1 이 아니면 1 리턴
    # 음수에서 비어있는 부분은 pass
    # 양수에서 1로 시작하지 않으면 1 리턴
    # 양수에서 비어 있는 숫자 리턴
    list_len = len(A)
    if list_len == 0:
        return 1
    if list_len == 1 and A[0] == 1:
        return 2

    sorted_A = sorted(A)
    cur_value = sorted_A[0]
    one_find = False
    for i in range(list_len):
        if cur_value == 1:
            one_find = True
        if cur_value < 1:
            pass
        else:
            if cur_value == sorted_A[i]:
                pass
            else:
                if cur_value + 1 == sorted_A[i]:
                    pass
                else:
                    if cur_value == -1 and sorted_A[i] == 1:
                        pass
                    else:
                        break

        cur_value = sorted_A[i]

    if one_find is True and cur_value > 0:
        return cur_value + 1
    return 1
    pass

print(solution([1, 1, 3]))                  # 2
print(solution([1, 93]))                    # 2
print(solution([-3, -2, -1]))               # 1
print(solution([-3, -2, -1, 1, 2]))         # 3
print(solution([-3, -2, -1, 2, 3]))         # 1
print(solution([2]))                        # 1
print(solution([3, 4]))                     # 1
print(solution([1, 2, 3]))                  # 4
print(solution([-1, -3]))                   # 1
print(solution([-3, -1, 1, 2, 3, 4, 5]))    # 6
#print(solution([]))
#print(solution([1]))
#print(solution([3]))
#print(solution([-5]))
