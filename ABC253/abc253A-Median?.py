import statistics
a,b,c=map(int,input().split())
if b ==statistics.median([a,b,c]):
    print('Yes')
else:
    print('No')

