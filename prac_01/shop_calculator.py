
def calculate_total_price(num_items, prices):
    total_price = sum(prices)
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

    return total_price

def main():
    num_items = int(input("Number of items: "))
    prices = []

    for i in range(num_items):
        price = float(input("Price of item {}: ".format(i + 1)))
        prices.append(price)

    total_price = calculate_total_price(num_items, prices)
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))

if __name__ == "__main__":
    main()
