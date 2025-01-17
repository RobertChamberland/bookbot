def main():
    book_path = "books/frankenstein.txt"   
    text = get_book_text(book_path)
    num_words = get_num_words(text)     #total number of words
    character_count = get_char_count(text)  # total number of alphabet characters only
    print(f"--- Begin report of {book_path} --- \n {num_words} words were found in the document \n \n {character_count} \n --- End report ---")

def get_char_count(text):
    char_dict = {}
    lowercase_text = text.lower()
    
    for character in lowercase_text:   
        if character.isalpha() == True: # check if it's a letter
            if character not in char_dict:  # add it to dict
                char_dict[character] = 1
            else:
                char_dict[character] += 1   # add to counter
        return char_dict

#goal: have characters sorted by number of appearances + print a report showing this.
# - sort the characters in the "char_key" by #
# - add wording to the print
    # - make it print the key entry
    # - make it print the key value
    # - have text between the two
        ## this may be a for loop in the print somehow? that way it cycles through each character

def sort_count(char_dict):
    #make list only include letters

    char_dict.sort(reverse=True, key=sort_count)
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
