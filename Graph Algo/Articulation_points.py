def dfs(node,par):
    global count
    global ti
    visited[node]=True
    low[node]=ti;f_time[node]=ti
    ti+=1
    child=0
    for i in graph[node]:
        if(i==par):
            continue
        if(visited[i]):
            low[node]=min(low[node],f_time[i])
        else:
            dfs(i,node)
            low[node]=min(low[node],low[i])
            if(f_time[node]<=low[i] and par!=-1):
                articulation[node]=0
            child+=1
    if(par==-1 and child>=2):
        articulation[node]=0
    
        
        
for _ in range(int(input())):
    n,m=map(int,input().split())
    graph={}
    for i in range(1,n+1):  graph[i]=[]
    
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[False for i in range(n+1)]
    low=[-1 for i in range(n+1)]
    f_time=[-1 for i in range(n+1)]
    ti=0;count=0
    articulation={}
    for  i in range(1,n+1):
        if(not visited[i]):
            dfs(i,-1)
    print(articulation.keys())

'''
2
5 5
1 2
1 3
3 2
3 4
5 4
7 6
1 2
2 3
2 4
2 5
3 6
3 7
'''
