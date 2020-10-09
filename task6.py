def find_long_words(string, word_length):
    words_list =  list(string.split(" "))
    new_list = []
    for item in words_list: 
        if len(item) >= word_length:
            new_list.append(item)
    print(new_list)