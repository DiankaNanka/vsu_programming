f1 = f2 = 1
 
n = int(input())
 
if n < 2:
    quit()
 
print(f1, end=' ')
print(f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
 
print()
