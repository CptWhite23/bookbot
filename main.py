def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    print(count_words(file_content))

def count_words(text):
    words = text.split()
    return len(words)

main()