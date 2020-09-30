R=[-1,1,0,0]
C=[0,0,-1,1]
from heapq import heappush,heappop
def dijkstra():
    x=[(0,0)]
    dis[0][0]=mat[0][0]
    while(True):
        boo=False
        h=[]
        for i in x:
            a=i[0];b=i[1]
            for j in range(4):
                r=a+R[j]
                c=b+C[j]
                if(0<=r<n and 0<=c<n):
                    heappush(h,(dis[a][b]+mat[r][c],(r,c),i))
    
        while(h):
            v=heappop(h)
            dis_2=dis[v[2][0]][v[2][1]]+mat[v[1][0]][v[1][1]]
            
            if(dis[v[1][0]][v[1][1]]>dis_2):
                boo=True
                dis[v[1][0]][v[1][1]]=dis_2
                x.append(v[1])
        if(not boo):
            break

    return dis[-1][-1]            
        
for _ in range(int(input())):
    n=int(input())
    temp=[int(i) for i in input().split()]
    mat=[];dis=[]
    for i in range(0,n*n,n):
        mat.append(temp[i:i+n])
        dis.append([1e9]*n)
    visited=[[False]*n for i in range(n)]
    ans=dijkstra()
    print(ans)
