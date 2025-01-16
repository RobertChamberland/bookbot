def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_count(text)
    print(character_count)

def get_char_count(text):
    char_dict = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict
            
def sort_count(char_dict):
    return char_dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
