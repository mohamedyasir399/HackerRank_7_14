if __name__ == '__main__':
    names,scores,lst=[],[],[]
    for _ in range(int(input())):
        name = input()
        names.append(name)
        score = float(input())
        scores.append(score)
    m =scores.index(min(scores))
    c = scores.count(min(scores))
    while c:
        m = scores.index(min(scores))
        scores.remove(min(scores))
        names.remove(names[m])
        c-=1
    m =min(scores)
    for i in range(len(scores)-1,-1,-1):
        if scores[i] == m:
            lst.append(names[i])
    lst.sort()
    for i in lst[:2]:
        print(i)
