import string

def main():
    # Opens the file
    with open('/home/stev/workspace/github.com/username/bookbot/books/MaryShellyFrankenstien', 'r') as f:
        contents = f.read()
        trans_table = str.maketrans('', '', string.punctuation + ' ' + '\n')
        clean_string = contents.translate(trans_table)
        words = clean_string.split()
        characters = clean_string
    print(f'The book contains {len(words)} words.')
        
    # Creates a dictionary for character frequency
    char_count = {}
    
          
    # Loops through the list of characters
    for character in characters:
        character = character.lower()
        # Increments the count for this character in the dictionary
        char_count[character] = char_count.get(character, 0) + 1
    
    # Sorts out and then prints the char_count dictionary in 
    for character, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{character}: {count}")


main()
