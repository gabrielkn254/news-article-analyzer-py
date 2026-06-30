from analyze import count_specific_word, identify_most_common_word
article = "Python is a high-level, interpreted programming language widely celebrated for its readability and simplicity. Created by Guido van Rossum and released in 1991, its design philosophy emphasizes clean code structure, often using indentation instead of curly braces to define code blocks. This user-friendly syntax makes it an exceptional choice for beginners learning to code, while its immense power and versatility attract seasoned developers worldwide. Today, Python serves as the foundational backbone for cutting-edge technologies, driving advancements in artificial intelligence, machine learning, data science, web development, and automation."

try:
    print(count_specific_word(article, "dog"))
    print(identify_most_common_word(article))
except ValueError as e:
    print("Validation Error:", str(e))