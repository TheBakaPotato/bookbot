import sys
from stats import worder_counter
from stats import letter_counter
from stats import char_num_dict_parse
the_path = ""
#the_path = "books/frankenstein.txt"
def get_book_test(the_path):
    with open(the_path) as f:
        the_content = f.read()
    return the_content

#report = "This is a report of the book stats"
# The report will include the number of words and the letter count
# and the character number dictionary parsed
# The report will be printed to the console
def get_report():
    counted_words = worder_counter(get_book_test(the_path))
    report = "============ BOOKBOT ============\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {counted_words} total words\n"
    report += "--------- Character Count -------\n"
    #iterates over the char_num_dict_parse function and add each letter and its count to the report
    char_num_dict = char_num_dict_parse(get_book_test(the_path))
    for char in char_num_dict:
        report += f"{char['char']}: {char['num']}\n"
    report += "============= END ===============\n"
    return report
def main():
    global the_path
    if len(sys.argv) > 1:
        a_path = sys.argv[1]
        the_path = a_path
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    letter_count = letter_counter(get_book_test(the_path))
    counter = worder_counter(get_book_test(the_path))
    text_out=get_book_test(the_path)
    worder_counter_v = f"{counter} words found in the document"
    char_num_dict_parse_v = char_num_dict_parse(get_book_test(the_path))
    reported = get_report()
    print(reported)
    #print(char_num_dict_parse_v)
main()