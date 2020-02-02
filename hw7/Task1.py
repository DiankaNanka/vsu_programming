#Variant_3

class Matrix:

    def __init__(self):
        self.strng = None
        self.column = None
        self.mtrx = []
        

    def rec(self):
        self.strng = int(input("Введи количество строк: "))
        self.column = int(input("Введи количество столбцов: "))
        for a in range(self.column):
            self.mtrx.append([int(input("Введи элемент матрицы: ")) for b in range(self.strng)])

    def output(self):
        print(self.mtrx, end='\n')

a = Matrix()
a.rec()
a.output()