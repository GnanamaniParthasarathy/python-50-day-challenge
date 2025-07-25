
# Count words, sentences, and characters in a paragraph

def count_text_stats(paragraph):
    # Count characters (excluding spaces if you want)
    characters = len(paragraph)
    
    # Count words (split by whitespace)
    words = len(paragraph.split())
    
    # Count sentences (basic split by ., ?, !)
    sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
    
    return words, sentences, characters

# Example usage
paragraph = input("Enter a paragraph: ")

words, sentences, characters = count_text_stats(paragraph)

print("Words:", words)
print("Sentences:", sentences)
print("Characters:", characters)
