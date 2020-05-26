def chislo():
    a = int(input("Введи число: "))
    for b in range(a, 1000):
        if a == b:
            if b%10 != 0:
                c = b%10
                if b/10 < c:
                    print(c)
            if b%100 != 0:
                d = b%100
                if b/10 < d:
                    print((b-b%10)/10)

chislo()
