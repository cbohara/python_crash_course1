def word_count(filename):
    """Count the approximate number of words in the file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['text_files/alice.txt', 'text_files/magic.txt', 'text_files/sid.txt']
for filename in filenames:
    word_count(filename)
