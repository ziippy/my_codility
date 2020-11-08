'''
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

class Solution { public int solution(int X, int[] A); }

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
'''
문제을 이해하지 못해서... X를 넘는 시간을 찾는 문제인가 해서 쉽게 풀었더니, 결과는 18% 만족.
그래서 문제 설명만 찾아봄
한마디로 1부터 X까지의 지점을 모두 거쳐서 X에 도달했다면, 해당 인덱스(초)를 리턴하는 것이다.
모두 거쳐야 한다는 걸 위에 영어만 봐서는 나는 이해하지 못했다. 
점프 라길래, 한방에 X로 점프 하는 건가 했지...ㅎ
'''
def solution(X, A):
    # write your code in Python 3.6
    # 일단 건너가야 하는 길이보다, array 의 길이가 더 작으면 불가하다.
    if len(A) < X:
        return -1

    # 아래와 같이 짜니 63% 만족. 복잡도는 O(N ** 2) 이었다.
    '''
    target_list = list(range(X+1))
    target_list.remove(0)
    for i, x in enumerate(A):
        try:
            target_list.remove(x)
        except:
            pass

        if len(target_list) == 0:
            return i
    return -1
    '''

    # 다르게 짜보자.
    # 이렇게 짜니 100% 만족. 복잡도는 O(N) 이었다.
    target_list = [0] * (X + 1)
    find_count = 0
    for i, x in enumerate(A):
        if target_list[x] == 0:
            target_list[x] = 1
            #
            find_count += 1
            if find_count == X:
                return i
    return -1
    pass

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))