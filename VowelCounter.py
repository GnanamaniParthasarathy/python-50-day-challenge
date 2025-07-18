
# Count vowels in a given word

# Get input from user
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize vowel count
count = 0

# Loop through each character in the word
for char in word:
    if char in vowels:
        count += 1

# Display the result
print(f"Number of vowels in '{word}': {count}")
