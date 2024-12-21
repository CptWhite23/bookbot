def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    print(count_words(file_content))
    print(count_chars(file_content))

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}

    for char in text:
        char_lowercase = char.lower()
        if char_lowercase in char_dict:
            char_dict[char_lowercase] += 1
        else:
            char_dict[char_lowercase] = 1
    
    return char_dict

main()