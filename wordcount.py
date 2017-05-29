def word_count(your_file):
    """counts the letters in a text file and prints the totals"""
    text_file = open(your_file)
    word_count = {}

    for line in text_file:
        for word in line.split():
            word_count[word] = 1
            #print word_count

        for word in word_count:
            if word in word_count:
                word_count[word] += 1
           # else:
            #    word_count[word] = 1
            print word_count

word_count('test.txt')
