# Example 1: f-string formatting
year = 1922
brand = "Gibson"
model = "L-5 CES"
cost = 16035.00

print(f"{year} {brand} {model} for about ${cost:,.2f}!")

# Example 2: Using a for loop with string formatting
for i in range(0, 201, 50):
    print(f"{i:>4}")