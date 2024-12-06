def get_user_input():
    # Asking for user details
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")

    # Neatly organizing the data
    print("\nUser Information Summary:")
    print("----------------------------")
    print(f"Name      : {name}")
    print(f"Age       : {age}")
    print(f"Favorite Color : {color}")
    print("----------------------------")

# Call the function to run the program
get_user_input()
