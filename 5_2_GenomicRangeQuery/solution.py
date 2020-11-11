'''
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

class Solution { public int[] solution(String S, int[] P, int[] Q); }

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
def solution(S, P, Q):
    # write your code in Python 3.6
    # 아래와 같이 짜면 62% 만족. Correctness 는 다 맞았는데, Performance 가 0 %, 복잡도는 O(N * M)
    '''
    list_str = list(S)
    min_impact_factor = []
    for i in range(len(P)):
        start_pos = P[i]
        end_pos = Q[i] + 1
        min_val = 99
        for j in range(start_pos, end_pos, 1):
            target_value = list_str[j]
            if target_value == 'A':
                min_val = 1
                break
            elif target_value == 'C' and min_val > 2:
                min_val = 2
            elif target_value == 'G' and min_val > 3:
                min_val = 3
            elif target_value == 'T' and min_val > 4:
                min_val = 4
                break
        min_impact_factor.append(min_val)

    return min_impact_factor
    '''

    # 다르게 짜보자.
    # 아래와 같이 짜도 62% 만족. Correctness 는 다 맞았는데, Performance 가 0 %, 복잡도는 O(N * M)
    '''
    import time
    aa = time.time()
    impact_factor = []
    for i in range(len(S)):
        target_value = S[i]
        if target_value == 'A':
            impact_factor.append(1)
        elif target_value == 'C':
            impact_factor.append(2)
        elif target_value == 'G':
            impact_factor.append(3)
        elif target_value == 'T':
            impact_factor.append(4)
    bb = time.time()
    print('Mid Elapsed: ', bb - aa)

    # print('impact_factor done')

    min_impact_factor = []
    for i in range(len(P)):
        #aa = time.time()
        start_pos = P[i]
        end_pos = Q[i] + 1
        min_val = min(set(impact_factor[start_pos:end_pos]))
        # print('min_val: ', min_val, ', i: ', i)
        min_impact_factor.append(min_val)
        #bb = time.time()
        #print('Mid Elapsed: ', i, ' - ', bb - aa)

    return min_impact_factor
    '''

    # 또 다르게 짜보자.
    # https://nachwon.github.io/GenomicRangeQuery/
    # 카운터 이용
    # 이렇게 하니 100% 만족, 복잡도는 O(N + M)
    # import time
    # aa = time.time()
    counter_list = [[0, 0, 0, 0]]
    counter_value = [0, 0, 0, 0]
    for i in range(len(S)):
        target_value = S[i]
        if target_value == 'A':
            counter_value[0] += 1
        elif target_value == 'C':
            counter_value[1] += 1
        elif target_value == 'G':
            counter_value[2] += 1
        elif target_value == 'T':
            counter_value[3] += 1
        counter_list.append(counter_value[:])
    # print(counter_list)

    # bb = time.time()
    # print('Mid Elapsed: ', bb - aa)

    # print('impact_factor done')

    min_impact_factor = []
    for i in range(len(P)):
        # aa = time.time()
        start_pos = P[i]
        end_pos = Q[i] + 1

        start_counter = counter_list[start_pos]
        # print(start_counter)
        end_counter = counter_list[end_pos]
        # print(end_counter)

        min_value = 1
        for j in range(4):
            if end_counter[j] - start_counter[j] >= 1:
                min_value = j + 1
                break

        min_impact_factor.append(min_value)
        # bb = time.time()
        # print('Mid Elapsed: ', i, ' - ', bb - aa)

    return min_impact_factor

    pass

#print(solution('CAGCCTA', [2], [2]))                # [3]
#print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))    # [2, 4, 1]
#print(solution('CT', [0], [0]))                     # [2]
print(solution('ACGT', [0, 1, 2, 3], [0, 1, 2, 3]))
print(solution('ACGT', [0, 1, 2, 3], [1, 2, 3, 3]))

#exit(0)


import random
string_pool = 'GGGG'
random_str = ''
max_str_len = 100000
for i in range(max_str_len):
    if i % 10 == 0:
        random_str += 'A'
    else:
        random_str += random.choice(string_pool)
# print(random_str)

query_len = 50000
p_list = []
q_list = []
for i in range(query_len):
    start_num = random.randint(0, query_len/2)
    p_list.append(start_num)
    end_num = random.randint(query_len/2, query_len)
    q_list.append(end_num if end_num >= start_num else query_len)
# print(p_list)
# print(q_list)

#random_str = 'CAGCCTA'

import time
a = time.time()
print(solution(random_str, p_list, q_list))
b = time.time()
print('Elapsed: ', b - a)
