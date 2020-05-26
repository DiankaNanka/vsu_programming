class Matrix:



    def __init__(self):

        self.st = 0

        self.column = 0

        self.m = []	

    def putin(self):

        self.row = int(input("Strins: "))

        self.column = int(input("Column: "))

        print("Elements: ")

        for a in range(self.column):

            self.m.append([input() for b in range(self.st)])

        print()



class Matrix2x2(Matrix):



    def check(self):

        if  self.st * self.column != 4:

            print("Matrix isn't 2x2")

        else:

            print("Matrix is 2x2")

            

            

example = Matrix2x2()

example.putin()

example.check()