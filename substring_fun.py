class SubStringFun:
    """
    Complete the function that takes an array of words.
    You must concatenate the nth letter from each word to construct a new word which should be returned as a string,
    where n is the position of the word in the list.
    Example:
    ["yoda", "best", "has"]  -->  "yes"
      ^        ^        ^
      n=0     n=1     n=2
    """

    @staticmethod
    def my_case(words):
        word = ""
        counter = 0
        for i in words:
            word += i[counter]
            counter += 1
        return word

    @staticmethod
    def best_practice(words):
        return ''.join(w[i] for i, w in enumerate(words))
