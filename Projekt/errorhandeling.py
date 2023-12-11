def get_valid_input(prompt):
    """A loop that checks whether user input can be converted to int, ends when successful"""
    
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")