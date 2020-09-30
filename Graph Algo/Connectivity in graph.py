n,e=map(int,input().split())
dic={}
for i in range(1,n+1):
    dic[i]=[]
boo=[False]*(n+1)
def bfs(dic,s,boo):
    q=[s]
    while(len(q)>0):
        v=q[0]
        #print(q,dic[v])
        q.pop(0)
        for i in dic[v]:
            if(not boo[i]):
                boo[i]=True
                q.append(i)
            
for i in range(e):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
count=0
for i in range(1,n+1):
    if(boo[i]==True):
        continue
    bfs(dic,i,boo)
    #print(boo)
    count+=1
print(count)
    
