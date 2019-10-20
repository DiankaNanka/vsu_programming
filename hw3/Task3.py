def fib(n):
    f1 = 0
    f2 = 1
    print(f1, end=' ')
    for i in range(1, n):
        f1, f2 = f2, f1 + f2
        print(f1, end = ' ')

        
n = int(input())
fib(n)

