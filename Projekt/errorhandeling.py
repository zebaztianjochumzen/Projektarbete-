def get_valid_input(prompt):
    """A loop that checks whether user input can be converted to int and checks so its positive, ends when successful"""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")