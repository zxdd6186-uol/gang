def get_ordered_list(numbers=None):
    if numbers is None:
        user_input = input("Enter a list of integers (comma-separated): ")
        numbers = [int(num.strip()) for num in user_input.split(",")]

    return sorted(numbers)