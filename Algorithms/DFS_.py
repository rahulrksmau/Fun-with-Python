def dfs(start):
    V[start] = True
    print start #dfs traversal of Graph
    for item in G[start]:
        if not V[item]:
            dfs(n,item)
            V[item] = True

def no_of_connected_component(s):
    Visited[s] = True
    for item in G[s]:
        if not Visited[item]:
            no_of_connected_component(item)

def initialize(N):
    for i in xrange(1,N+1):
        G[i] = []

def main():
    global G
    global Visited
    G = {}
    N,V = map(int,raw_input().split())
    initialize(N)
    Visited = [False]*(N+1)
    for _ in xrange(V):
        a,b = map(int, raw_input().split())
        G[a].append(b)
        G[b].append(a)
    
    print G
    #dfs(n,1) #Method for dfs traversal
    n = 0
    for i in xrange(1,N+1):
        if not Visited[i]:
            no_of_connected_component(i)
            n += 1
    print n

if __name__=="__main__":
    main()

