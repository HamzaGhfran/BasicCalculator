class Calculator:
    def __init__(self):
        self.num1 = input("Enter First Number:")
        self.num2 = input("Enter Second Number:")
    
    def multiplication(self):
        print (int(self.num1) * int(self.num2))

    def _addition(self):
        print(int(self.num1) + int(self.num2))
    
    def _subtraction(self):
        print(int(self.num1) - int(self.num2))

p1 = Calculator()
p1.multiplication()
p1._addition()