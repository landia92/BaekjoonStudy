def solution(arr1, arr2):
    r1=len(arr1)
    c1=len(arr1[0])
    # 행렬의 곱은 앞의 열 == 뒤의 행 경우만 가능
    # 행렬의 곱으로 만들어지는 배열은 앞의 행 * 뒤의 열
    # r2=len(arr2)
    c2=len(arr2[0])
    arr = [[0]*c2 for x in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                arr[i][j]+=arr1[i][k]*arr2[k][j]
            
    answer = arr
    return answer