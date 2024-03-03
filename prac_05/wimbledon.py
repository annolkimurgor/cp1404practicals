"""
Wimbledon Champions
File: wimbledon.py
"""


def read_data(filename):
    """Reads data from the given filename and returns a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            line = line.strip().split(",")
            data.append(line)
    return data


def get_champions(data):
    """Returns a dictionary of champions and their number of wins."""
    champions = {}
    for entry in data:
        champion = entry[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Returns a set of countries of the champions."""
    countries = set()
    for entry in data:
        country = entry[1]
        countries.add(country)
    return countries


def main():
    filename = "wimbledon.csv"
    data = read_data(filename)

    champions = get_champions(data)
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    countries = get_countries(data)
    sorted_countries = sorted(countries)
    print("\nThese", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))


if __name__ == "__main__":
    main()

