#Remember;;;;;;;;;;;;;;;;;
#This code is based on 0th indexing of the graph.. you can change that

def dfs(node,G):
    global t
    visited[node]=True
    stack=[node];count=[frev[node]]
    while(len(stack)>0):
        sink=True
        x=stack[-1]
        for i in G[x]:
            if(not visited[i]):
                count.append(frev[i])
                stack.append(i)
                visited[i]=True
                sink=False
        if(sink):
            #print(stack)
            v=stack.pop()
            f_time[v]=t
            t+=1
    return count
for _ in range(int(input())):
    n,m=map(int,input().split())
    t=0;s=-1
    visited=[False for i in range(n)]
    f_time=[0 for i in range(n)]
    frev=[0 for i in range(n)]
    leader=[None for i in range(n)]
    graph={};rev={}
    for i in range(n):
        graph[i]=[]
        rev[i]=[]
    temp=[int(i) for i in input().split()]
    for i in range(0,2*m,2):
        if(temp[i+1] not in graph[temp[i]]):
            graph[temp[i]].append(temp[i+1])
            rev[temp[i+1]].append(temp[i])
    for i in range(n-1,-1,-1):
        if(not visited[i]):
            s=i
            dfs(i,rev)
    for i in range(n):
        frev[f_time[i]]=i
    new_g={}
    for i in range(n):
        new_g[f_time[i]]=[]
        for j in graph[i]:
            new_g[f_time[i]].append(f_time[j])
    ans=[]
    visited=[False for i in range(n)]
    for i in range(n-1,-1,-1):
        if(not visited[i]):
            temp=dfs(i,new_g)
            ans.append(temp)
    for i in ans:
        print(*i)
    
    
    
    
    
    
    
    
    
    
    
    
