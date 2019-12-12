#!/usr/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    ac = len(argv)

    if (ac != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    opc = argv[2]

    if opc == '+':
        res = add(a, b)
    elif opc == '-':
        res = sub(a, b)
    elif opc == '*':
        res = mul(a, b)
    elif opc == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, opc, b, res))
