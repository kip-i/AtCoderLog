def make_divisors(n,a):
    num=0
    i = 1
    N=n*n
    while i*i <= N:
        if N % i == 0:
            num=num+1
            if i != N // i:
                num=num+1
                if a<(N//i):
                    num=num-2
        i += 1
    return num
def main():
    n = int(input())
    num=0
    for i in range(1,n+1):
        num=num+make_divisors(i,n)

    print(num)
    return 0
main()
