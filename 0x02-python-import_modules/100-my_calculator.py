#!/usr/bin/python3
import calculator_1
import sys

if __name__ == '__main__':
    argv = sys.argv
    n = len(argv)

    if n != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        oprand = argv[2]

        oprators = ["+", "-", "*", "/"]
        if oprand not in oprators:
            print("Unknown oprator. Available oprators: +, -, * and /")
            sys.exit(1)
        else:
            if oprand == "+":
                print(f"{a} {oprand} {b} = {calculator_1.add(a, b)}")

            elif oprand == "-":
                print(f"{a} {oprand} {b} = {calculator_1.sub(a, b)}")

            elif oprand == "*":
                print(f"{a} {oprand} {b} = {calculator_1.mul(a, b)}")

            elif oprand == "/":
                print(f"{a} {oprand} {b} = {calculator_1.div(a, b)}")
            sys.exit(0)
