def solution(citations):
    answer = 0
    citations.sort()
    cLen=len(citations)
    for i in range(0, cLen+1):
        count=0
        for j in range(cLen):
            if i<=citations[j]:
                count+=1
        if count>=i and cLen-count<=i:
            answer=i
    return answer