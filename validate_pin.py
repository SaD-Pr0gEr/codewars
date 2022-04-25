class ValidatePin:
    """
    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits
    or exactly 6 digits.
    If the function is passed a valid PIN string, return true, else return false.
    Examples:
    "1234"   -->  true
    "12345"  -->  false
    "a234"   -->  false
    """

    @staticmethod
    def my_method(pin: str) -> bool:
        try:
            if int(pin) < 0 or len(pin.split("\n")) > 1 or len(pin.split("+")) > 1 or len(pin.split(" ")) > 1:
                return False
            return True if (len(list(pin)) == 4 or len(list(pin)) == 6) else False
        except ValueError:
            return False

    @staticmethod
    def best_practise(pin):
        return len(pin) in (4, 6) and pin.isdigit()
