"""Creating a gui Calculator with the help of Red."""


class Calculator:

    num1: float
    num2: float

    #   I don't understand this line, I wouldnt be able to explain it.
    def __init__(self, num1: float, num2: float) -> None:
        self.num1 = num1
        self.num2 = num2

    #   the method below will add the two numbers num1 and num2 before returning the result
    def add(self) -> float:
        return self.num1 + self.num2
    
        # the method below will subtract the two numbers num1 and num2 before returning the result
    def subtract(self) -> float:
        return self.num1 - self.num2
    
        # the method below will multiply the two numbers num1 and num2 before returning the result
    def multiply(self) -> float:
        return self.num1 * self.num2
    
        # the method below will divide the two numbers num1 and num2 before returning the result
    def divide(self) -> float:
        return self.num1 / self.num2
    
        # the method below will return the exponent of the two numbers(num1, num2)
    def exponent(self) -> float:
        return self.num1 ** self.num2
    
        # the method below will return the remainder of the two numbers(num1, num2)
    def remainder(self) -> float:
        return self.num1 // self.num2
    
def main():
    try:
        num1 = float(input('Input the first number: '))
        operation = input('Input the operation: ')
        num2 = float(input('Input the second number: '))

        calculator: Calculator = Calculator(num1, num2)
        if operation == '+':
            print(f'The result is: {calculator.add()}')
        elif operation == '-':
            print(f'The result is: {calculator.subtract()}')
        elif operation == '*':
            print(f'The result is: {calculator.multiply()}')
        elif operation == '/':
            print(f'The result is: {calculator.divide()}')
        elif operation == '**':
            print(f'The result is: {calculator.exponent()}')
        elif operation == '//':
            print(f'The result is: {calculator.remainder()}')
        else:
            raise ValueError(f'The provided operation {operation} is not supported, please use +, -, *, /, **, //')
            
    except Exception as e:
        print(e)
        exit(code=1)


if __name__ == '__main__':
    main()