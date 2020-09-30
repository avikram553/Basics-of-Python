def dfs(node):
    global aid
    stack.append(node)
    chk[node]=True
    visited[node]=True
    ids[node]=aid;low[node]=aid
    aid+=1
    for i in graph[node]:
        if(not visited[i]):
            dfs(i)
        if(chk[i]): low[node]=min(low[node],low[i])
    
    if(ids[node]==low[node]):
        temp=[]
        while(1):
            no=stack.pop()
            temp.append(no)
            chk[no]=False
            low[no]=ids[node]
            if(no==node):
                break
        ans.append(temp)
    return low
            
for _ in range(int(input())):
    n,m=map(int,input().split())
    
    graph={}
    temp=[int(i) for i in input().split()]
    for i in range(n):  graph[i]=[]
    for i in range(0,2*m,2):
        if(temp[i+1] not in graph[temp[i]]):
            graph[temp[i]].append(temp[i+1])
    aid=0;ans=[]
    visited=[False for i in range(n)]
    chk=[False for i in range(n)]
    stack=[]
    low=[0 for i in range(n)]
    ids=[-1 for i in range(n)]
    for i in range(n):
        if(not visited[i]):
            dfs(i)
    for i in ans:
        print(*i,end=',')
    print()
    
