q = int(input())
s={}
for i in range(q):
    l=input().split()
    if l[0]=='1':
        if int(l[1]) not in s.keys():
            s[int(l[1])]=1
        else:
            s[int(l[1])]=s[int(l[1])]+1
    elif l[0]=='2':
        if int(l[1]) in s.keys():
            if int(l[1])>=s[int(l[1])]:
              del s[int(l[1])]
            else:
                s[int(l[1])]=s[int(l[1])]-int(l[1])
    else:
        print(max(s)-min(s))




