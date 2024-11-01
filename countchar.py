def count_chars(text):
    char_counts = {}
    text = text.lower()  # Hace minisculas
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def count_chars(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Abre y lee el libro
with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
    book_text = file.read()

# Usa funcion en el libro
result = count_chars(book_text)

print(result)
