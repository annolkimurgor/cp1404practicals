def display_menu(name):
    print("Hello, {}!".format(name))
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def main():
    name = input("Enter name: ")
    choice = ""

    while choice != "Q":
        display_menu(name)
        choice = input(">>> ")

        if choice == "H":
            print("Hello {}".format(name))
        elif choice == "G":
            print("Goodbye {}".format(name))
        else:
            print("Invalid choice")

    print("Finished.")

if __name__ == "__main__":
    main()