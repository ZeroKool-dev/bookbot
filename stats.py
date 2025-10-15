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