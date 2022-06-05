q = int(input())
s=[]
for i in range(q):
    l=input().split()
    if l[0]=='1':
        s.append(int(l[1]))
    elif l[0]=='2':
        popl=[]
        for j in range(len(s)):
            if s[j]==int(l[1]) and len(popl)<=int(l[2]):
                popl.append(j)
            if len(popl)>int(l[2]):
                break
        for j in range(min([int(l[2]),len(popl)])):
            s.pop(popl[j]-j)
    else:
        print(max(s)-min(s))




