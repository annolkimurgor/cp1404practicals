import random

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    print(determine_result(user_score))

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print("Random Score:", random_score)
    print("Result for Random Score:", determine_result(random_score))

if __name__ == "__main__":
    main()
