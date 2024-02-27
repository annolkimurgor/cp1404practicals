def main():
    password = get_password()
    print_password_stars(password)


def get_password():
    return input("Enter your password: ")


def print_password_stars(password):
    print("*" * len(password))


if __name__ == "__main__":
    main()
