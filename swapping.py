class CaseSwapping:
    """
    Given a string, swap the case for each of the letters.
    e.g. CodEwArs --> cODeWaRS
    """

    @staticmethod
    def my_method(string_) -> str:
        new_string = list(string_)
        data = []
        for i in new_string:
            if i.islower():
                data.append(i.upper())
            else:
                data.append(i.lower())
        return "".join(data)

    @staticmethod
    def best_practise(string_: str):
        return string_.swapcase()
