class Calculator:
    
        """
        This class is used to perform basic arthmathic operations (+, -, *, /)
        over two integers.
        In this  class input get by user.
        """
        def __init__(self):
            self.num1 = input("Enter First Number:")
            self.num2 = input("Enter Second Number:")
        
        def multiplication(self):
            print (int(self.num1) * int(self.num2))

        def addition(self):
            print(int(self.num1) + int(self.num2))
        
        def subtraction(self):
            print(int(self.num1) - int(self.num2))

