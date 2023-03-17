from Logical import *
from Arthmitic import *


def Input(opr):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if opr == "+":
        return  sum(a,b)
    elif opr == "-":
        return  sub(a,b)
    elif opr == "*":
        return  mul(a,b)
    elif opr == "/":
        return  div(a,b)
    elif opr == ">":
        return  max(a,b)
    elif opr == "<":
        return  min(a,b)
    elif opr == "==":
        return  equal(a,b)
    elif opr == "!=":
        return  not equal(a,b)
    else:
        return  "Invalid operator"

def output(*args):
    print(str(args[0]))
