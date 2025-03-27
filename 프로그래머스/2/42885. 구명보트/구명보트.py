def solution(people, limit):
    people.sort()
    count = 0
    start=0
    end=len(people)-1
    while start < end:
        if people[start] + people[end] <= limit:
            count +=1
            start += 1
            end -= 1
        elif people[start] + people[end] > limit:
            count +=1
            end -= 1
    if start == end:
        count+=1
    answer = count
    return answer