## 풀이한 문제 ⚒️
- 입력받은 문자열의 각 문자를 입력받은 정수만큼 입력해 새 문자열을 출력하는 문제

## 소요 시간 🛩️
- [X] 1시간 미만
- [ ] 1~3시간
- [ ] 3시간 이상

## 문제풀이 중점사항 🤔
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num, alpha = input().split() 
    num = int(num) 
    alpha = str(alpha) 

// 입력받은 문자열(alpha)의 한 인덱스를 num을 곱한 만큼 출력
    for i in range(len(alpha)):
        print(num * alpha[i], end='')
    print()

## 그 외 추가 리서치 🚀
- (자유롭게 관련된 의견 내용 및 참고한 자료를 공유해 주세요)

