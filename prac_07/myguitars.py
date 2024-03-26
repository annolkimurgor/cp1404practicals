from guitar import Guitar


def read_guitars_from_csv_file():
    # Read guitars from a CSV file and return a list of Guitar objects
    guitars = []
    file = open('guitars.csv', 'r')
    for line in file:
        name, year, cost = line.strip().split(',')
        guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def write_guitars_to_csv_file(guitars):
    file = open('guitars.csv', 'w')
    for guitar in guitars:
        file.write(repr(guitar) + '\n')


def display_guitars(guitars):
    # Display the list of guitars
    for guitar in guitars:
        print(guitar)


def main():
    guitars = read_guitars_from_csv_file()

    # Prompt users to enter new guitars
    while True:
        name = input("Enter guitar name: ")
        if name.lower() == "":
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    # Sort guitars by year
    guitars.sort()

    display_guitars(guitars)

    # write guitars to CSV file
    write_guitars_to_csv_file(guitars)
    print("Guitars written to 'guitars.csv'")


if __name__ == "__main__":
    main()
