import collections
def solution(queue1, queue2):
    answer = 0
    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)
    target = (sum(q1) + sum(q2))/2
    while(q1 and q2 and sum(q1) != target):
        if sum(q1) > sum(q2):
            q2.append(q1.popleft())
        else:
            q1.append(q2.popleft())
        answer += 1
    if not q1 or not q2 or sum(q1) != target:
        answer = -1
    return answer