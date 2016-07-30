def word_count(filename):
    """Count the approximate number of words in the file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # failing silently
        # 'pass' statement tells Python to do nothing in this block
        # acts as a placeholder in case we do want to do something here in the future,
        # like write any missing filenames into a file called missing_files.txt
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['text_files/alice.txt', 'text_files/magic.txt', 'text_files/sid.txt']
for filename in filenames:
    word_count(filename)
