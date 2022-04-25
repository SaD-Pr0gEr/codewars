class LongWordFilter:
    """
    Write a function that takes a string and an an integer n as parameters and returns a list of all words that
    are longer than n.
    Example:
    * With input "The quick brown fox jumps over the lazy dog", 4
    * Return ['quick', 'brown', 'jumps']
    """

    @staticmethod
    def my_case(sentence, n):
        return [i for i in sentence.split() if len(i) > n]

    @staticmethod
    def filter_long_words(sentence, long):
        return [word for word in sentence.split() if len(word) > long]
