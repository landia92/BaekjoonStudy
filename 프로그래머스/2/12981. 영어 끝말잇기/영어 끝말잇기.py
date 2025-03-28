def solution(n, words):
    sWords = set(words)
    count = {}
    answer = []
    err=0
    for x in range(len(words)):
        if x > 0 and x < len(words)-1:
            if words[x-1][-1] != words[x][0]:
                err = x+1
                break
                
    if len(words) != len(sWords):
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    err=j+1
                    break
    
    if err == 0:
        answer = [0, 0]
    else:
        if err%n==0:
            answer = [n, err//n]
        else:
            answer = [err%n, err//n+1]
    return answer