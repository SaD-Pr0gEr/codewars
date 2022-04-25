
class DomainSplit:
    """
    Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
    Example:
        domain_name("http://github.com/carbonfive/raygun") == "github"
    """

    @staticmethod
    def my_case(url):
        domain_split = url.split("//")[-1].split("/")[0]
        return domain_split.split(".")[0] if "www" not in domain_split else domain_split.split(".")[1]

    @staticmethod
    def best_practice(url):
        return url.split("//")[-1].split("www.")[-1].split(".")[0]
