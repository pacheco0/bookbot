def read_file(frankenstein):
    with open(frankenstein, 'r') as file:
        return file.read()
content = read_file("books/frankenstein.txt")

def count_words(text):
    words = text.split()
    return len(words)

word_count = count_words(content)
print(word_count)
