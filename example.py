# import fucntion modules from analyze package
from analyze import count_specific_word, identify_most_common_word, calculate_average_word_length, count_paragraphs, count_sentences

# You can use this sample text to test this program.
sample_text = """Python is a high-level. interpreted programming language. widely celebrated for its readability and simplicity.
Created by Guido van Rossum and released in 1991. its design philosophy emphasizes clean code structure. often using indentation instead of curly braces to define code blocks."""

# APP MENU

print("Article Analyzer")
while True:
    print("\nMENU:\ni.e Type '1' if choice is 'Count specific word'\n\n1. Count specific word\n2. Identify Most Common Word\n3. Calc average word length\n4. Count Number of Paragraphs\n5. Count Number Sentences\n\nType '0' to exit")
    choice = input(": ")
    if int(choice) == 1:
        print("Choosed 1: Count specific word\n")
        article = input("Submit article: ")
        print("\n")
        word = input("Word to count: ")
        try:
            print("\nCount: ", count_specific_word(article, word), "\n-----------------")
        except ValueError as e:
            print("Validation Error: ", str(e), "\n-----------------")
        input("Type anything to go back to main menu: ")
        continue        
    elif int(choice) == 2:
        print("Choosed 2: Identify most common word\n")
        article = input("Submit article: ")
        print("\nCommon word: ", identify_most_common_word(article), "\n-----------------")
        input("Type anything to go back to main menu: ")
        continue
    elif int(choice) == 3:
        print("Choosed 3: Calc average word length\n")
        article = input("Submit article: ")
        print("\nAverage: ", calculate_average_word_length(article), "\n-----------------")
        input("Type anything to go back to main menu: ")
        continue
    elif int(choice) == 4:
        print("Choosed 4: Count Number of paragraphs\n")
        article = input("Submit article: ")
        print("\nNo. of paragraphs: ", count_paragraphs(article), "\n-----------------")
        input("Type anything to go back to main menu: ")
        continue
    elif int(choice) == 5:
        print("Choosed 5: Count number of sentences\n")
        article = input("Submit article: ")
        print("\nNo. of sentences: ", count_sentences(article), "\n-----------------")
        input("Type anything to go back to main menu: ")
        continue
    elif int(choice) == 0:
        print("Goodbye")
        break
    else:
        print("\nInput Error: Invalid choice")
        continue