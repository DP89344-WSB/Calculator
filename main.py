from calculator import Calculator

def main():
    calc = Calculator()
    
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(5, 3))
    print("Multiplication:", calc.multiply(5, 3))
    print("Division:", calc.divide(5, 3))

if __name__ == "__main__":
    main()
