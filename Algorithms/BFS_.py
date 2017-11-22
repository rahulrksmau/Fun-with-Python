#Graph BFS traversal

def dfs(G,n,V):
    queue = [n]
    while queue:
        e = queue.pop(0)
        print "{0}->".format(e),
        for item in G[e]:
            if not V.get(item,False):
                queue.append(item)
                V[item] = True
                    
def main():        
    G = {
        1:[2,11,8],
        2:[1,14,7],
        11:[1,17,6],
        8:[1],
        14:[2],
        7:[2],
        17:[11],
        6:[11]
        }
    V = {1:True}
    head_node = 1
    dfs(G,head_node,V)
    
if __name__ == "__main__":
    main()
