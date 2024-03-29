class CreatePhoneNumber:
    """
    Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
    the form of a phone number.
    Example:
        create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
    """

    @staticmethod
    def my_case(n):
        n.insert(0, "(")
        n.insert(4, ")")
        n.insert(5, " ")
        n.insert(9, "-")
        return "".join(map(str, n))

    @staticmethod
    def best_practice(n):
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
