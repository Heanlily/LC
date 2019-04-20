import collections
def f(lis):
    temp=[]
    for i in range(len(lis[0])):
        temp.append([lis[0][i],lis[1][i]])
    print(temp)
    hash={}
    k=0
    for i in range(len(temp)):
        if temp[i][0] not in hash:
            hash[temp[i][0]]=k
            k+=1
        if temp[i][1] not in hash:
            hash[temp[i][1]]=k
            k+=1

    father=list(range(100000))
    def find(x):
        while x!=father[x]:
            x=father[x]
        return x
    def union(x,y):
        father[find(x)]=find(y)

    for i in range(len(temp)):
        union(hash[temp[i][0]],hash[temp[i][1]])

    res=collections.defaultdict(list)
    for i in hash:
        res[find(hash[i])].append(i)
    return res
lis=[["abc","abc","abc"],["bcd","acd","def"]]
print(f(lis))

