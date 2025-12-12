class Calculator:
    def calculate(self, a: float, b: float, operation: str) -> float:
        if operation == "add":
            return a + b
        elif operation == "sub":
            return a - b
        elif operation == "mul":
            return a * b
        elif operation == "div":
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            return a / b
        else:
            raise ValueError("Unsupported operation")

calc = Calculator()
print(calc.calculate(10.0, 5.0, "add"))  
print(calc.calculate(10.0, 5.0, "div"))  
