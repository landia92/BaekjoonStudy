def solution(n, left, right):
    # arr=[[0] * n for x in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if j<i:
    #             arr[i][j]=i+1
    #         else:
    #             arr[i][j]=j+1
    num=right-left+1
    answer = [0]*num
    x=left
    # l1=left//n
    # l2=left%n
    # r1=right//n
    # r2=right%n
    for i in range(num):
        x1=x//n
        x2=x%n
        if x1>x2:
            answer[i]=x1+1
        else:
            answer[i]=x2+1
        x+=1
    return answer