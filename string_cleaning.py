class StringCleaning:
    """
    Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers.
    Your program will take in a string and clean out all numeric characters, and return a string with spacing and
    special characters ~#$%^&!@*():;"'.,? all intact.

    Examples:
        '! !'                 -> '! !'
        '123456789'           -> ''
        'This looks5 grea8t!' -> 'This looks great!'
    """

    @staticmethod
    def my_case(s):
        """
        Function will return the cleaned string
        """
        return "".join([i for i in s if i.isalpha() or i in "~#$%^&!@*():;\"'.,? "])

    @staticmethod
    def best_practice(s):
        return ''.join(x for x in s if not x.isdigit())
