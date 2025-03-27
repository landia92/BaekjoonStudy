def solution(n):
    n2 = format(n, 'b')
    num = n2.count('1')
    for i in range(n+1,1000001):
        i2 = format(i, 'b')
        if i2.count('1') == num:
            return i
            break
    