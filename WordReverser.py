
# Reverse individual words in a sentence

# Get input from user
sentence = input("Enter a sentence: ")

# Split sentence into words and reverse each word
reversed_words = [word[::-1] for word in sentence.split()]

# Join and display the result
reversed_sentence = ' '.join(reversed_words)
print(f"Reversed words: {reversed_sentence}")
