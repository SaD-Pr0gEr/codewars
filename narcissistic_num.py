class NarcissticNumber:
    """
     A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the
     number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10)
     For example, take 153 (3 digits), which is narcisstic:
     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """

    @staticmethod
    def my_method(value: int) -> bool:
        counter = 0
        for i in list(str(value)):
            counter += int(i) ** len(list(str(value)))
        return counter == value

    @staticmethod
    def best_practise(value):
        return value == sum(int(x) ** len(str(value)) for x in str(value))
