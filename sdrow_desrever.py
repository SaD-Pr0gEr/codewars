class ReversedWords:
    """
    Complete the solution so that it reverses all of the words within the string passed in.
    "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
    """

    @staticmethod
    def my_case(s):
        return " ".join((s.split()[::-1]))

    @staticmethod
    def best_practice(string):
        return " ".join(string.split(" ")[::-1])
