def main():
    book_path = "books/frankenstein.txt"   
    text = get_book_text(book_path)
    num_words = get_num_words(text)     #total number of words
    character_count = get_char_count(text)  # total number of alphabet characters only
    sorted_list = sort_count(character_count)

    print(f"--- Begin report of {book_path} --- ") #Prints report title
    print(f"{num_words} words were found in the document\n") #prints number of words
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"The '{char}' charcter was found {count} times")
    print("--- End report ---")



def get_char_count(text):
    char_dict = {}
    lowercase_text = text.lower()
    
    for character in lowercase_text:   
        if character.isalpha(): # check if it's a letter (don't need to put == True since ".isalpha" already has that check built in)
            char_dict[character] = char_dict.get(character, 0) + 1 #checks the character, returns its value if it exists (otherwise assigns 0 as value), then increments by 1
        
    # Convert dictionary to list of dictionaries
    char_list = [{"char": char, "num": num} for char, num in char_dict.items()]
    return char_list

def sort_count(char_list): 
    return sorted(char_list, key=lambda x: x["num"], reverse=True)
    # for above, lambda returns "num"'s value in the dict
    # reverse makes it in order of big to small
    # sorted returns a new sorted list (vs sort() which would sort the current list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
