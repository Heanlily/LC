def f_dfs(lis):
    res=[]
    isvisited=set()

    def dfs(i,temp):
        for j in range(len(lis)):
            if lis[i][j] and j not in isvisited:
                isvisited.add(j)
                temp.append(j)
                dfs(j,temp)

    for i in range(len(lis)):
        if i not in isvisited:
            temp=[]
            dfs(i,temp)
            res.append(temp)
    return res

def f_bfs(lis):
    isvisited=set()
    res=[]
    def bfs(i,temp):
        queue=[i]
        while queue:
            n=queue.pop(0)
            temp.add(n)
            for i in range(len(lis)):
                if lis[n][i] and i not in isvisited:
                    isvisited.add(i)
                    queue.append(i)
        return temp

    for i in range(len(lis)):
        if i not in isvisited:
            temp=set()
            res.append(bfs(i,temp))
    return len(res)

