def next_greater(l):
    temp = [0]
    for i in xrange(1,len(l)):
        while len(temp) and l[i] > l[temp[-1]]:
            l[temp.pop()]=l[i]
        temp.append(i)
    for i in temp:
        l[i] = -1
    return None


def main():
    for _ in range(int(input())):
        n   = int(input())
        arr = map(int,raw_input().split())
        #print ("Before execution : ", arr)
        next_greater(arr)
        #print ("After execution : ", arr)
        for i in arr:
            print i,
            
if __name__ == "__main__":
    main()
