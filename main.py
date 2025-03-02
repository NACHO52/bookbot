from stats import get_num_words
from stats import get_num_app
from stats import get_sorted_dic
import sys

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_book_text(url)
    num_words = get_num_words(content)
    diccionario = get_num_app(content)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sortedDic = get_sorted_dic(diccionario)
    for dic in sortedDic:
        if dic["letter"].isalpha():
            print(f"{dic['letter']}: {dic['count']}")
    print("============= END ===============")
    

main()