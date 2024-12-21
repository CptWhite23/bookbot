def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    print_report(file_content)

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

def print_report(text):
    words = count_words(text)
    character_dict = count_chars(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")

    for key in character_dict:
        print(f"The '{key}' character was found {character_dict[key]} times")

    print("--- End report ---")

main()