def get_num_words(words):
    num_words = len(words.split())
    print(f"Found {num_words} total words")

def get_count_by_char(words):
    char_dict = {}
    char_list = []
    for word in words:
        for character in word.lower():
            if character in char_dict:
                char_dict[character]+=1
            elif character.isalpha():
                char_dict[character]=1
    for i in char_dict:
        char_list.append({"char":i,"num":char_dict[i]})
    char_list.sort(reverse=True,key=sort_on)
    for j in char_list:
        print(j['char'] + ": " + str(j['num']))

def sort_on(items):
    return items["num"]
