'''
    BOJ 9252 LCS
    최장 공통 부분문자열의 길이와 그 내용을 출력
    - N <= 1,000
    - DP approach 사용(O(N^2))
'''

a = input()
b = input()

LCS = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if i == 0 or j == 0:  # 마진 설정
            LCS[i][j] = 0
        elif a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
max_len = LCS[len(a)][len(b)]
if max_len == 0:
    print(0)
else:
    print(max_len)
    ret = []
    i = len(a)
    j = len(b)
    while True:
        if LCS[i][j] == 0:
            break
        elif LCS[i][j] == LCS[i-1][j]:
            i -= 1
            continue
        elif LCS[i][j] == LCS[i][j-1]:
            j -= 1
            continue
        else:
            ret.append(a[i-1])
            i -= 1
            j -= 1
    print(''.join(ret[::-1]))