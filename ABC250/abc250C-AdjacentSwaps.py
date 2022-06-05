n,q = map(int, input().split())
l = list(range(n))#位置におけるボール番号
b = list(range(n))#各ボールの位置
for _ in range(q):
    num1 = int(input())-1
    l1 = b[num1]
    if l1 == n-1:
       l2=l1-1
    else:
        l2=l1+1
    num2 = l[l2]
    l[l1],l[l2]=num2,num1
    b[num1],b[num2]=l2,l1
print(*[i+1 for i in l])
"""
for _ in range(q):
    num1 = int(input())
    l1 = l[num1-1]
    if l1 == n-1:
       l2=l1-1
    else:
        l2=l1+1
    num2 = b[l2]
    l[l1],l[l2]=l[l2],l[l1]
    b[l1],b[l2]=b[l2],b[l2]
print(*[i+1 for i in l])
"""


