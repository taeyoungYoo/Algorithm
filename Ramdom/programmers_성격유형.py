from collections import defaultdict


def solution(survey, choices):
    character = defaultdict(int)
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    for idx, sur in enumerate(survey):
        if choices[idx] > 4:
            character[sur[1]] += scores[choices[idx]]
        else:
            character[sur[0]] += scores[choices[idx]]

    ret = ""
    if character['T'] > character['R']:
        ret += 'T'
    else:
        ret += 'R'
    if character['F'] > character['C']:
        ret += 'F'
    else:
        ret += 'C'
    if character['M'] > character['J']:
        ret += 'M'
    else:
        ret += 'J'
    if character['N'] > character['A']:
        ret += 'N'
    else:
        ret += 'A'
    return ret
