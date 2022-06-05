def main():
    n,k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b=a[:]
    b.sort()
    if a==b:
        print('Yes')
        return 0
    num=len(a)
    for i in range(num-k):
        f=0
        for j in range(0,num-k-i):
            if a[j]>a[j+k]:
                a[j],a[j+k]=a[j+k],a[j]
                f=f+1
        if f==0 :
            if a==b:
                print('Yes')   
            else:
                print('No')
            return 0
    if a==b:
        print('Yes')
    else:
        print('No')
main()