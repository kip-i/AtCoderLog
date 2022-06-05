h,w = map(int, input().split())
s = [input() for i in range(h)]

a=[]
b=[]
fl=0
for i in range(h):
    for j in range(w):
        if s[i][j]=="o":
            if fl==0:
                a=[i,j]
                fl=1
            else:
                b=[i,j]
                break
if a[1]<b[1]:
    n=b[1]-a[1]+b[0]-a[0]
else:
    n=b[0]-a[0]+a[1]-b[1]
print(n)

