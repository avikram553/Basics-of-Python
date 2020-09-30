n,e=map(int,input().split())
graph={};count=1
st=[0]*(n+1)
boo=[False]*(n+1)
def dfs(graph,s):
    global count
    global boo
    stack=[s]
    boo[s]=True
    for i in graph[s]:
        if(not boo):
            dfs(graph,i)
    #print(s,boo)
    st[s]=count
    count+=1


    
for i in range(1,n+1):
    graph[i]=[]
for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
for i in range(1,n+1):
    if(not boo[i]):
        dfs(graph,i)
print(st)
