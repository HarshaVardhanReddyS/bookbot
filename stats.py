def get_book_text(path):
    with open(path) as f:
        filecontents = f.readlines()
        count = 0
        for line in filecontents:
            count += len(line.split())
        return f'Found {count} total words'

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    chars = []
    for char in dict:
        chars.append({'name': char, 'num': dict[char]})
    # print(chars)
    chars.sort(reverse= True, key=sort_on)
    return chars
    
def count_chars(path):
    dict_chars = {}
    file_content = ""
    with open(path) as f:
        file_content = f.read().lower()
    for char in file_content:
        if len(char) == 1 and char.isascii() and char.isalpha():
            if char not in dict_chars:
                dict_chars[char] =  int(1)
            else:
                dict_chars[char] += int(1)
    return sorted_list(dict_chars)