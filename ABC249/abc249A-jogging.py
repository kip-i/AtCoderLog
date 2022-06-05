a,b,c,d,e,f,x = map(int, input().split())
m1=int(x/(a+c))
ma1=int(x%(a+c))
m2=int(x/(d+f))
ma2=int(x%(d+f))
if ma1>a:
    ma1=a
if ma2>d:
    ma2=d
y1=m1*b*a+ma1*b
y2=m2*e*d+ma2*e
if y1==y2:
    print("Draw")
elif y1>y2:
    print("Takahashi")
else:
    print("Aoki")