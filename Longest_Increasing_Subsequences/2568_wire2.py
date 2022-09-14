import collections
from bisect import bisect_left


n = int(input())
input_dict = collections.defaultdict(int)
cvt_input = collections.defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    input_dict[a] = b
    cvt_input[b] = a
input_dict = dict(sorted(input_dict.items()))

wire1 = list(input_dict.keys())
wire2 = list(input_dict.values())

def LIS_LIST(cand_list : list) -> list:
    tmp = []
    index = [0] * len(cand_list)
    tmp.append(cand_list[0])
    for i in range(1, len(cand_list)):
        if tmp[-1] < cand_list[i]:
            index[i] = len(tmp)
            tmp.append(cand_list[i])
        else:
            replace_idx = bisect_left(tmp, cand_list[i])
            tmp[replace_idx] = cand_list[i]
            index[i] = replace_idx
    max_index = max(index)
    ret = []
    for i in range(len(index)-1, -1, -1):
        if index[i] == max_index:
            ret.append(cand_list[i])
            max_index -= 1
        if max_index < 0:
            break
    return ret[::-1]

lis = LIS_LIST(wire2)
print(len(wire2) - len(lis))
for i in range(len(wire2)):
    if wire2[i] not in lis:
        print(wire1[i])