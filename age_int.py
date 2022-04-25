class ParseInt:
    """
    Ask a small girl - "How old are you?". She always says strange things... Lets help her!
    For correct answer program should return int from 0 to 9.
    Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.
    """

    @staticmethod
    def my_case(age):
        return int(age.split(" ")[0])

    @staticmethod
    def best_practice(age):
        return int(age[0])
