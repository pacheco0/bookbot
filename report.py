with open('books/frankenstein.txt', 'r') as file:
    text = file.read()

words = text.split()
word_count = len(words)

char_count = {}

for char in text:
    if char.isalpha():  # Check if the character is a letter
        char = char.lower()  # Convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Convert the dictionary to a list of tuples (char, count)
sorted_char_count = sorted(char_count.items(), 
key=lambda item: item[1], reverse=True)

print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")

for char, count in sorted_char_count:
    print(f"The '{char}' character was found {count} times")

print(f"--- End report ---")

