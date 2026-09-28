import unittest


def is_even(number):
    return number % 2 == 0


def calculate_discount(price, percent):
    # This implementation contains a defect for students to find with a test.
    return price * (1 + percent / 100)


def format_name(first_name, last_name):
    return f"{last_name.strip()}, {first_name.strip()}"


class TestFunctions(unittest.TestCase):
    def test_is_even(self):
        # TODO: Test an even number and an odd number.
        pass

    def test_calculate_discount(self):
        # TODO: Test a discount calculation.
        pass

    def test_format_name(self):
        # TODO: Test the expected "Last, First" format.
        pass


if __name__ == "__main__":
    unittest.main()
