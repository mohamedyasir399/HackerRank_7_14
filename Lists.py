if __name__ == '__main__':
    N = int(input())
    lst=[]
    for x in range(N):
        n = input().split()
        if n[0] == "insert":
            lst.insert(int(n[1]),int(n[2]))
        elif n[0] == 'print':
            print(lst)
        elif n[0] == "remove":
            lst.remove(lst[0])
        elif n[0] == 'append':
            lst.append(int(n[1]))
        elif n[0] =='sort':
            lst.sort()
        elif n[0]== 'pop':
            lst.pop(-1)
        elif n[0] == 'reverse':
            lst.reverse()
