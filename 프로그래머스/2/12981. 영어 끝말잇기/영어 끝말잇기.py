def solution(n, words):
    count = {}
    answer = []
    err=0
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            answer = [i%n+1, i//n+1]
            return answer
        else:
            answer = [0, 0]
    return answer