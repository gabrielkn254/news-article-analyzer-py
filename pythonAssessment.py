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
        raise ValueError("Empty article")
    clean_article = re.sub(r"[^\w\s]", "", article)
    words = clean_article.split()
    return words.count(word.lower())

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
    max_word_appearances = max(words_count.values())
    most_common_words = [word for word, count in words_count.items() if count == max_word_appearances]
    return " ".join(most_common_words)

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
    paragraphs = re.split("\n+", article.strip())
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
    raw_sentences = re.split(r"(?<=[.!?])\s+", article.strip())
    sentences = [s for s in raw_sentences if re.search(r"[a-zA-Z0-9]", s)]
    return len(sentences)

# sample article test
text = """Python is a high-level. interpreted programming language. widely celebrated for its readability and simplicity.
Created by Guido van Rossum and released in 1991. its design philosophy emphasizes clean code structure. Often using indentation instead of curly braces to define code blocks."""

while True:
    try:
        print("Count: ", count_specific_word(text, "code"))
    except ValueError as e:
        print("Validation Error:", str(e))

    print("Common word: ", identify_most_common_word(text))
    print("Average: ", calculate_average_word_length(text))
    print("No. of paragraphs: ", count_paragraphs(text))
    print("No. of sentences: ", count_sentences(text))
    break