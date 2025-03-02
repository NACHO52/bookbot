
def get_num_words(text:str):
    return len(text.split())

def get_num_app(text:str):
    result = {}
    for t in text.lower():
        if t not in result:
            result[t] = 0
        result[t] += 1
    return result

def get_sorted_dic(alphabet):
    result = []
    for letter in alphabet:
        result.append({"letter": letter, "count": alphabet[letter]})
    result.sort(key=lambda letter: letter["count"], reverse=True)
    return result