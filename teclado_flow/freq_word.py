with open('words.txt') as input_file:
    words=''
    for line in input_file:
        words += line.strip().lower()

    words=words.split(' ')
    unique_words_set=set(words)
    unique_words=list(unique_words_set)
    unique_words.sort()
    freq_words = {}
    max_freq_word=''
    max_freq=1
    for word in unique_words:
        freq_words[word]=words.count(word)
        if words.count(word)>max_freq:
            max_freq=words.count(word)
            max_freq_word=word


    print(max_freq_word, max_freq)
    print(freq_words)