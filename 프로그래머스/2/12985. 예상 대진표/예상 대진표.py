def solution(n,a,b):
    bn=0
    sn=0
    count=0
    answer=0
    if a>b:
        bn=a
        sn=b
    else:
        bn=b
        sn=a
    while bn!=sn:
        if bn%2==1:
            bn=bn+1
        if sn%2==1:
            sn=sn+1
        bn=bn/2
        sn=sn/2
        count=count+1
    answer = count
    return answer