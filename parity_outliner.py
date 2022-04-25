class ParityOutliner:
    """
    You are given an array (which will have a length of at least 3, but could be very large) containing integers.
    The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
    integer N. Write a method that takes the array as an argument and returns this "outlier" N.
    """

    @staticmethod
    def my_case(integers):
        num = [i for i in integers if i % 2 == 0]
        num2 = [i for i in integers if i % 2 != 0]
        return num[0] if len(num) == 1 else num2[0]

    @staticmethod
    def best_practice(int):
        odds = [x for x in int if x % 2 != 0]
        evens = [x for x in int if x % 2 == 0]
        return odds[0] if len(odds) < len(evens) else evens[0]
