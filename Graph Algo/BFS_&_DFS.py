def BFS(l):
    q=[];dic={}
    q.append(1)
    dic[1]=0
    while(len(q)!=0):
        s=q.pop(0)
        print(s,end=' ')
        for j in l[s]:
            if(j not in dic.keys()):
                q.append(j)
                dic[j]=0
BFS({1:[2,3],2:[1,4,5],3:[1,5],4:[2,5,6],5:[2,3,4,6],6:[4,5]})

#-----------------------------------------------------------------------------------        
def DFS(l):
    q=[];dic={}
    q.append(1)
    dic[1]=0
    while(len(q)!=0):
        s=q.pop(-1)
        print(s,end=' ')
        for j in l[s]:
            if(j not in dic.keys()):
                q.append(j)
                dic[j]=0
        #print(q)
print()
print("######################")
DFS({1:[3,2],2:[1,4,5],3:[1,5],4:[2,5,6],5:[3,6],6:[4,5]})

#-----------------------------------------------------------------------------------

def BFS_short_path(l,fr0m,t0):
    q=[];dic={}
    q.append(fr0m);boo=False
    dic[fr0m]=0
    while(len(q)!=0):
        s=q.pop(0)
        for j in l[s]:
            if(j not in dic.keys()):
                q.append(j)
                dic[j]=dic[s]+1
                if(j==t0):
                    boo=True
        if(boo):
            break
        
    c=dic[t0] if(t0 in dic.keys())  else -1
    print(c)
    #print(dic)
print()
print("######################")
BFS_short_path({1:[3,2],2:[1,4,5],3:[1,5],4:[2,5,6],5:[3,6],6:[4,5]},1,6)
        
