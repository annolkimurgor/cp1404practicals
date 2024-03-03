"""
Emails and Names Storage
File: emails.py
"""


def extract_name(email):
    """Extracts the name from an email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(part.title() for part in parts)
    return name


def main():
    emails_dict = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        name = extract_name(email)
        if email in emails_dict:
            print(f"Email '{email}' already exists with name '{emails_dict[email]}'")
            continue
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == '' or confirmation == 'y':
            emails_dict[email] = name
        else:
            name = input("Name: ").strip().title()
            emails_dict[email] = name

    print("\nStored Emails and Names:")
    for email, name in emails_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
