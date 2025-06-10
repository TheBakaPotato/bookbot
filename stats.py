def worder_counter(book_string_content):
    worder=book_string_content.split()
    counter=len(worder)
    return counter
def letter_counter(book_string_content):
    book_string_content = book_string_content.lower()
    letter_count = {}
    for letter in book_string_content:
        if letter not in letter_count and letter.isalpha():
            letter_count[letter] = 0
    for char in book_string_content:
        for letter in letter_count:
            if char == letter:
                letter_count[letter] += 1
    return letter_count
def char_num_dict_parse(book_string_content):
    letter_counter_dict = letter_counter(book_string_content)
    char_num_list = []
    #iterate through the letter_counter_dict dictionary
    for letter, count in letter_counter_dict.items():
        #create a tuple of a dictionary with the letter and its count
        char_num_list.append({"char": letter, "num": count})
    #sort the list of dictionaries by the greater num value
    char_num_list.sort(key=lambda x: x["num"], reverse=True)
    return char_num_list
