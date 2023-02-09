class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def multiplication(self):
        print(self.num1 * self.num2)

p1 = Calculator(5, 6)
p1.multiplication()