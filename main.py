def main():
    with open('/home/stev/workspace/github.com/username/bookbot/books/MaryShellyFrankenstien', 'r') as f:
        contents = f.read()
        words = contents.split()
        print(f'The book contains {len(words)} words.')

main()
