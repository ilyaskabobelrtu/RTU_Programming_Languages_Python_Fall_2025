"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    char_count = len(text)
    words = text.split()
    word_count = len(words)
    text_lower = text.lower()
    has_python = "python" in text_lower
    return (char_count, word_count, has_python)
    pass

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    sentence = input("Enter a sentence: ")
    result = analyze_sentence(sentence)
    chars, words, python_check = result
    print("Character count:", chars)
    print("Word count:", words)
    if python_check:
        print("Contains 'Python': Yes")
    else:
        print("Contains 'Python': No")
    pass
