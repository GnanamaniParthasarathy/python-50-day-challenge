
# Shift each letter in a word by 1 position in the alphabet

def shift_letters(word):
    shifted = ""
    for char in word:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            # Shift by 1 with wrap-around using modulo
            shifted += chr((ord(char) - base + 1) % 26 + base)
        else:
            shifted += char  # Keep non-alphabet characters unchanged
    return shifted

# Example usage
word = input("Enter a word or sentence: ")
print("Shifted:", shift_letters(word))
