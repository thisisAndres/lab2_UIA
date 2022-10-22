import math


class calculos():
    def __init__(self):
        self.workedH = None
        self.pricePerH = None
        self.Usu = None
        self.Num = None
        self.str = None

    def calcSalary(self):
        self.workedH = int(
            input("Please type the amount of hours yout've worked\n"))
        self.pricePerH = int(
            input("Please type how much you earn per hour.\n"))
        calc = self.pricePerH * self.workedH
        print(f"Worked hours: {self.workedH}.\n" +
              f"Price per hour: {self.pricePerH}.\n" +
              f"The total amount you'll receive is: {calc}")

    def printName(self):
        self.usu = input("Please type your name\n")

        print(f"Bienvenido a la UIA {self.usu.lower()}\n" +
              f"Bienvenido a la UIA {self.usu.upper()}")

    def elevate(self):
        self.Num = int(input('Type the number to be elevated\n'))

        if (self.Num >= 1 and self.Num <= 10):
            print(f"Elevated by 2: {math.pow(self.Num, 2)}")

        elif (self.Num >= 11 and self.Num <= 20):
            print(f"Elevated by 4: {math.pow(self.Num, 4)}")

        elif (self.Num >= 21 and self.Num <= 30):
            print(f"Elevated by 6: {math.pow(self.Num, 6)}")

        elif (self.Num >= 31 and self.Num <= 40):
            print(f"Elevated by 8: {math.pow(self.Num, 8)}")

        elif (self.Num >= 41 and self.Num <= 50):
            print(f"Elevated by 10: {math.pow(self.Num, 10)}")

        else:
            print(f"Not valid option: {0}")

    def primeNumber(self):
        self.Num = int(
            input("Please type the number you want to know if is\nprime number or not\n"))

        def isPrime(num):
            for i in range(2, num):
                if (num % i == 0):
                    return False
            return True

        if (isPrime(self.Num)):
            print(f"{self.Num} es un numero primo.")

        else:
            print(f"{self.Num} no es un numero primo.")

    def countStr(self):
        self.str = input("Type the string you want to count\n")
        print(
            f"The phrase '{self.str.lower()}' has {self.str.count('a')} 'a' ")
