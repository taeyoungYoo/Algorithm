'''
    프로그래머스 모의고사
    - 완전탐색 접근
'''


# index pointer 활용 풀이
def solution(answers):
    answer = [0, 0, 0]

    cand_1 = [1, 2, 3, 4, 5]
    cand_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    cand_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 사람에 대한 포인터 지정
    pnt_1 = pnt_2 = pnt_3 = 0
    # answers 완전탐색
    for i in range(len(answers)):
        if cand_1[pnt_1] == answers[i]:
            answer[0] += 1
        if cand_2[pnt_2] == answers[i]:
            answer[1] += 1
        if cand_3[pnt_3] == answers[i]:
            answer[2] += 1
        # 포인터 처리
        pnt_1 += 1
        pnt_2 += 1
        pnt_3 += 1
        if pnt_1 == 5:
            pnt_1 = 0
        if pnt_2 == 8:
            pnt_2 = 0
        if pnt_3 == 10:
            pnt_3 = 0
    # 동점자가 있는 경우와 없는 경우 나눠서 처리
    ret = []
    for i in range(3):
        if answer[i] == max(answer):
            ret.append(i+1)
    return ret


# 나머지를 통한 풀이
def solution(answers):
    answer = [0, 0, 0]

    cand_1 = [1, 2, 3, 4, 5]
    cand_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    cand_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # answers 완전탐색
    for idx, ans in enumerate(answers):
        if cand_1[idx % len(cand_1)] == ans:
            answer[0] += 1
        if cand_2[idx % len(cand_2)] == ans:
            answer[1] += 1
        if cand_3[idx % len(cand_3)] == ans:
            answer[2] += 1

    # 정답 정리
    ret = []
    for i in range(3):
        if answer[i] == max(answer):
            ret.append(i+1)
    return ret