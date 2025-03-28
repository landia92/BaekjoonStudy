def solution(n):
    arr = [0] * n
    if n <= 1:
        arr[0]=1
    elif n <= 2:
        arr[0]=1
        arr[1]=2
    else:
        arr[0]=1
        arr[1]=2
    if n > 2:
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
            
    answer = arr[n-1] % 1234567
    return answer
