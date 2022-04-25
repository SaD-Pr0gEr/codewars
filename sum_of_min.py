class SumOfMinimums:
    """
    Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
    your task is to find the sum of the minimum values in each row.
    Example:
    arr = [
        [ 1, 2, 3, 4, 5 ],        #  minimum value of row is 1
        [ 5, 6, 7, 8, 9 ],        #  minimum value of row is 5
        [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
    ]
    So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.
    """

    @staticmethod
    def my_case(numbers: list) -> int:
        mins = []
        [mins.append(min(i)) for i in numbers]
        return sum(mins)

    @staticmethod
    def best_practice(numbers):
        return sum(map(min, numbers))
