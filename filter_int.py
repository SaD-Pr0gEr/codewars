class IntFilter:
    """
    In this kata you will create a function that takes a list of non-negative integers and strings and returns a
    new list with the strings filtered out.
    Examples:
    input -> [1,2,'a','b'] output -> [1,2]
    """

    @staticmethod
    def my_case(num_list: list) -> list:
        return [i for i in num_list if type(i) is int]

    @staticmethod
    def best_practise(num_list: list):
        return [i for i in num_list if not isinstance(i, str)]
