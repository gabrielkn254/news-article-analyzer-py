import re

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

# Calculate the average length of words
def calculate_average_word_length(article):
    """
    This function calculates the average word length in the string `article.
    It doesn't count punctuation marks & special characters as word.

    args:
        article: a string you want scan.
    
    raises:
        No Error when you either pass an empty article but returns 0.
    """
    if not article:
        return 0
    clean_article = re.sub(r"[^\w\s]", "", article)
    words = clean_article.split()
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

# Count the number of paragraphs
def count_paragraphs(article):
    """
    This function counts the number of paragraphs in the text `article.
    It returns 1 for an empty string.

    args:
        article: a string you want scan.
    
    raises:
        No Error when you either pass an empty article but returns 1.
    """
    if not article:
        return 1
    paragraphs = re.split("\n", article)
    return len(paragraphs)

# Count the number of sentences
def count_sentences(article):
    """
    This function counts the number of sentences in the text `article.
    It returns 1 for an empty string.

    args:
        article: a string you want scan.
    
    raises:
        No Error when you either pass an empty article but returns 1.
    """
    if not article:
        return 1
    sentences = re.split(r"(?<=[.!?])\s+", article)
    return len(sentences)