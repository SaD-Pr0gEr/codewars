class Palindrome:
    """
    A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.
    Examples of numerical palindromes are:
        2332
        110011
        54322345
    For a given number num, write a function to test if it's a numerical palindrome or not and return a
    boolean (true if it is and false if not).
    Return "Not valid" if the input is not an integer or less than 0.
    """

    @staticmethod
    def my_case(num):
        return bool(str(num) == str(num)[::-1]) if type(num) == int and int(num) > 0 else "Not valid"

    @staticmethod
    def best_practice(num):
        if type(num) is not int or num < 1:
            return "Not valid"
        return num == int(str(num)[::-1])
