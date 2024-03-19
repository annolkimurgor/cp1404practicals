from guitar import Guitar


def test_guitar_methods():
    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test for get_age()
    expected_age = 100
    actual_age = Gibson.get_age(2022)
    print(f"{Gibson.name} get_age() - Expected {expected_age}. Got {actual_age}")

    # Test for is_vintage()
    expected_vintage = True
    actual_vintage = Gibson.is_vintage(2022)
    print(f"{Gibson.name} is_vintage() - Expected {expected_vintage}. Got {actual_vintage}")

    # Tesst for another Another Guitar
    another_guitar = Guitar("Another Guitor", 1922, 16035.40)

    # Test for get_age()
    expected_age = 9
    actual_age = another_guitar.get_age(2022)
    print(f"{another_guitar.name} get_age() - Expected {expected_age}. Got {actual_age}")

    # Test for is_vintage()
    expected_vintage = False
    actual_vintage = another_guitar.is_vintage(2022)
    print(f"{another_guitar.name} is_vintage() - Expected {expected_vintage}. Got {actual_vintage}")


test_guitar_methods()
