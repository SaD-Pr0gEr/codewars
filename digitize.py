class Digitize:
    """
    Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

    Example:
        348597 => [7,9,5,8,4,3]
        0 => [0]
    """

    @staticmethod
    def my_case(n):
        return [int(i) for i in str(n)][::-1]

    @staticmethod
    def best_practice(n):
        return map(int, str(n)[::-1])
