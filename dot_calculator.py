class DotCalc:
    """
    You have to write a calculator that receives strings for input. The dots will represent the number in the equation.
    There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.
    Here are the following valid operators :
    + Addition
    - Subtraction
    * Multiplication
    // Integer Division
    Examples:
    * "..... + ..............." => "...................."
    * "..... - ..."             => ".."
    * "..... - ."               => "...."
    * "..... * ..."             => ".........
    """

    @staticmethod
    def my_case(txt):
        left, operator, right = txt.split()
        if operator == "+":
            res = len(left) + len(right)
        elif operator == "-":
            res = len(left) - len(right)
        elif operator == "*":
            res = len(left) * len(right)
        else:
            res = len(left) // len(right)
        return res * "."

    @staticmethod
    def best_practice(txt):
        a, op, b = txt.split()
        a, b = len(a), len(b)
        return '.' * eval(f'{a} {op} {b}')
