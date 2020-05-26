def triangle():
    a = int(input("Введите 1 сторону треугольника: "))
    b = int(input("Введите 2 сторону треугольника:"))
    c = int(input("Введите 3 сторону треугольника:"))
    if (a+b) <= c or (a+c) <= b or (b+c) <= a:
        print("false")
    else:
        print("true")
triangle()