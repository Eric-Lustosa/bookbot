

def get_book_text(filepath):   
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_book_char(file_contents):
    dic_char = {}
    for i in file_contents:
        i_lower = i.lower()
        if i_lower in dic_char:
            dic_char[i_lower] = dic_char.get(i_lower, 1) + 1
        else:
            dic_char[i_lower] = 1
    return dic_char


#def sort_on(dic):
    #return dic[a]
           
def get_dict_list(dic):
    dic_list = []

    for chave in dic:
        dic_aux = {}
        value = dic[chave]
        dic_aux[chave] = value
        dic_list.append(dic_aux)

    sorted_items = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]) , reverse = True)

    return sorted_items

def print_report(sorted_items,file_contents):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words(file_contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_items:
        if item[0].isalpha() == True:
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")  






    
    
