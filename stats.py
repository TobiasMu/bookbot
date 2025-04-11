
def count_words(string):
    words = len(string.split())
    # print(words)

    return words

def count_symbols(string):
    dict = {}
    for i in string:
        i = i.lower()
        if i in dict.keys():
            dict[i] +=1
        else:
            dict[i]=1
    return dict
def report(dictionary):
    list_of_dicts=[]
    for key, value in dictionary.items():
        if key.isalpha():
            new_dict= {"symbol": key,
                       "count": value}
            list_of_dicts.append(new_dict)
    def sort_on(dict):
        return dict["count"]
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts


