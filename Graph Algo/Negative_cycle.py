import sys


def negative_cycle(adj):
    dis={};m=1000000
    for i in range(1,len(adj)+1):
        dis[i]=m
    n=len(adj)
    x=0;neg=False
    while(True):
        boo=False
        for i in adj.keys():
            for j in adj[i].keys():
                if(dis[j]>dis[i]+adj[i][j]):
                    boo=True
                    dis[j]=dis[i]+adj[i][j]
        if(not boo):
            break
        x+=1
        if(x>=n):
            neg=True
            break   
    return int(neg)

n,m=map(int,input().split())
adj = [[] for _ in range(n)]
adj={}
for i in range(1,n+1):
    adj[i]={}
for i in range(m):
    a=[int(i) for i in input().split()]
    adj[a[0]][a[1]]=a[2]
    print(negative_cycle(adj))
