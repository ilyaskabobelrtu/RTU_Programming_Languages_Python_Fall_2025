"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    # TODO: implement cleaning and formatting
    clean_name = name.strip()
    clean_name = clean_name.capitalize()
    return "Hello, " + clean_name + "! Welcome to Python!"
    pass

if __name__ == "__main__":
    # TODO: read name from input and print greeting
    name = input("Type your name?")
    message = greet_user(name)
    print(message)
    pass
