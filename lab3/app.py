import os
import getpass
import ast
import operator as op
# import re

## Izvor: https://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_expression(expr):
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)
##

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        # if self.b == 0:
        #     return float("nan")
        return self.a / self.b


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", eval_expression(expression))


if __name__ == "__main__":
    root_password = os.environ.get("ROOT_PASSWORD")
    if not root_password:
        print("ROOT_PASSWORD is not set!")
        exit(2)
    if len(root_password) < 6:
        print("ROOT_PASSWORD must have at least 6 characters!")
        exit(2)
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or password != root_password:
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()

