if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    c =arr.count(max(arr))
    while c:
        arr.remove(max(arr))
        c -=1
    print(max(arr))
