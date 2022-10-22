import calculos as calc

calc = calc.calculos()


class menu():
    option = ""
    while option != "6":
        option = input("Select the option you want:\n" +
                       "1 - Calculate salary\n" +
                       "2 - Write name\n" +
                       "3 - Elevate given number\n" +
                       "4 - Check if if a number is prime\n" +
                       "5 - Contar 'a' en cadenas de texto\n" +
                       "6 - EXIT\n")

        if (option == "1"):
            calc.calcSalary()

        elif (option == "2"):
            calc.printName()

        elif (option == "3"):
            calc.elevate()

        elif (option == "4"):
            calc.primeNumber()

        elif (option == "5"):
            calc.countStr()

        elif (option == "6"):
            pass

        else:
            print("Not valid option")
