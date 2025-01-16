def solution(park, routes):
    for idx1 in range(len(park)):
        for idx2 in range(len(park[idx1])):
            if(park[idx1][idx2]=='S'):
                p1=idx1
                p2=idx2
                break
    for r1 in range(len(routes)):
        idx1=p1
        idx2=p2
        if(routes[r1][0]=='E'):
            for n in range(int(routes[r1][2])):
                p2+=1
                if(p2>=len(park[idx1])):
                    p2=idx2
                    break
                elif(park[p1][p2]=='X'):
                    p2=idx2
                    break
        elif(routes[r1][0]=='W'):
            for n in range(int(routes[r1][2])):
                p2-=1
                if(p2<0):
                    p2=idx2
                    break
                elif(park[p1][p2]=='X'):
                    p2=idx2
                    break
        elif(routes[r1][0]=='S'):
            for n in range(int(routes[r1][2])):
                p1+=1
                if(p1>=len(park)):
                    p1=idx1
                    break
                elif(park[p1][p2]=='X'):
                    p1=idx1
                    break
        elif(routes[r1][0]=='N'):
            for n in range(int(routes[r1][2])):
                p1-=1
                if(p1<0):
                    p1=idx1
                    break
                elif(park[p1][p2]=='X'):
                    p1=idx1
                    break
    
    answer=[p1, p2]
    return answer