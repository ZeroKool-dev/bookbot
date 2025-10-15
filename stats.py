def get_num_words(text):
    """
    Counts the number of words in a given text.

    Parameters:
        text (str): The input text.

    Returns:
        int: The word count.
    """
    words = text.split()
    return len(words)

def get_num_characters(text):
    """
    Counts the number of characters in a given text.

    Parameters:
        text (str): The input text.

    Returns:
        int: The character count.
    """
    lower_case_text = text.lower()
    char_count = {}
    for char in lower_case_text:
        if char not in [' ', '\n', '\t']:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count