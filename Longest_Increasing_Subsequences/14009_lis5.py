from bisect import bisect_left


def LIS_binary(cand_list : list) -> list:
    tmp = []
    index = []
    tmp.append(cand_list[0])
    index.append(0)
    for i in range(1, len(cand_list)):
        if tmp[-1] < cand_list[i]:
            index.append(len(tmp))
            tmp.append(cand_list[i])
        else:
            replace_idx = bisect_left(tmp, cand_list[i])
            tmp[replace_idx] = cand_list[i]
            index.append(replace_idx)
    ret = []
    max_index = max(index)
    for i in range(len(cand_list)-1, -1, -1):
        if index[i] == max_index:
            max_index -= 1
            ret.append(cand_list[i])
    return ret[::-1]

def solution():
    n = int(input())
    input_list = list(map(int, input().split()))
    ret = LIS_binary(input_list)
    print(len(ret))
    print(' '.join(map(str, ret)))

solution()