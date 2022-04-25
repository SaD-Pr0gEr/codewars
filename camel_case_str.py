class CamelCaseStr:
    """
    Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
    All words must have their first letter capitalized without spaces.
    For instance:
        camelcase("hello case") => HelloCase
        camelcase("camel case word") => CamelCaseWord
    """

    @staticmethod
    def my_case(text):
        return "".join([i.capitalize() for i in text.split()])

    @staticmethod
    def best_practice(string):
        return string.title().replace(" ", "")
