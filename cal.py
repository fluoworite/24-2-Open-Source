
def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul (a, b):
    return a*b

def div (a, b):
    return a/b

if __name__ == "__main__":
    a = int(input("input integer number1 : "))
    op = input("input oponent :")
    if op not in ['*', '/', '+', '-']:
        print("Invalid Operator")
        exit()
    b = int(input("input integer number2 : "))

    if op == '+':
        print(f"Result: {add(a, b)}")
    elif op == '-':
        print(f"Result: {sub(a, b)}")
    elif op == '*':
        print(f"Result: {mul(a, b)}")
    elif op == '/':
        print(f"Result: {div(a, b)}")
    