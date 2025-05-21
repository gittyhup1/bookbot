def num_words(text):
    split_words = text.split()
    word_count = len(split_words)
    return word_count

def count_chars(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char not in char_dict.keys():
            char_dict[char] = 1
        elif char in char_dict.keys():
            char_dict[char] += 1
    
    return char_dict

def sort_key(dict):
    return dict["num"]

def format_char(char_dict):
    formatted_dict_list = []
    for key, value in char_dict.items():
        new_dict = {"char": key, "num": value}
        formatted_dict_list.append(new_dict)
        formatted_dict_list.sort(reverse=True, key=sort_key)
    return formatted_dict_list