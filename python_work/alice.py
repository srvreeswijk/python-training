file = 'alice_in_wonderland.txt'

try: 
    with open(file, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('bestand niet gevonden')
else:
    # Count the number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"There are {num_words} words in the file")