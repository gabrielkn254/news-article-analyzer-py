# Counts how many times a word has appeared
def count_specific_word(article, word):
    """
    This function determines how many times a `word` appears in the string `article.
    Note: This matches the exact word i.e article: appear, word: ear, doesn't match.
    It is not case sensitive

    args:
        article: the string with many words.
        word: the string you want to determine how many times the word appeared in article.
    
    raises:
        Value Error when you either pass an empty article or word argument.
    """
    if not article or not word:
        raise ValueError("Please pass a valid article & word")
    return str(article).lower().split().count(word.lower())

# Finds the common word
def identify_most_common_word(article):
    """
    This function determines which is the most common word in the string `article.
    It is not case sensitive

    args:
        article: a string you want scan.
    
    raises:
        No Error when you either pass an empty article but returns None.
    """
    if not article:
        return None
    words = article.lower().split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return max(words_count, key=words_count.get)