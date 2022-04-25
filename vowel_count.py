class VowelCount:
    """
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces.
    """

    @staticmethod
    def my_case(sentence: str) -> int:
        return len([i for i in list(sentence) if i in ("a", "i", "u", "e", "o")])

    @staticmethod
    def best_practise(input_str):
        return sum(1 for let in input_str if let in "aeiouAEIOU")
