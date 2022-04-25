class DropCaps:
    """
    DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, just like you see in the newspaper.
    But for a change, let"s do that for each and every word of the given String. Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.
    *should work also on Leading and Trailing Spaces and caps.
    "apple"            => "Apple"
    "apple of banana"  => "Apple of Banana"
    "one   space"      => "One   Space
    "   space WALK   " => "   Space Walk   "
    Note: you will be provided atleast one word and should take string as input and return string as output.
    """

    @staticmethod
    def my_case(str_):
        return " ".join(list(map(lambda a: a.capitalize() if len(a) > 2 else a, str_.split(" "))))

    @staticmethod
    def best_practice(str_):
        return ' '.join(w.capitalize() if len(w) > 2 else w for w in str_.split(' '))
