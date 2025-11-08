"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    # TODO: implement
    count = 0
    for char in text:
        if char != ' ':
            count = count + 1
    return count
    pass

def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    words = text.split()
    return len(words)
    pass

def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers
    pass

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)
    total = sum(nums)
    if nums:
        average = total / len(nums)
    else:
        average = 0
    return chars, words, nums, total, average
    pass

if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    user_text = input("Enter text: ")
    c, w, n, t, a = analyze_text(user_text)
    print("Characters (no spaces):", c)
    print("Words:", w)
    print("Numbers:", n)
    print("Sum:", t)
    print("Average:", a)
    pass
