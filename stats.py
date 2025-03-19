
#Lê arquivo.txt dentro do diretório books e retorna uma string que contem todo o texto do livro
def get_book_text(filepath):   
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

#Usando o comando split armazena em uma variável uma lista com todas as palavras do livro em seguida conta-se a quantidade de palavras usando a função len
def get_book_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words
#É preenchido um dicionário vazio, sendo as chaves cada character existente no livro e o seu valor associado sendo o número de vezes que ele aparece no livro
def get_book_char(file_contents):
    dic_char = {}
    for i in file_contents:
        i_lower = i.lower() #Transforma em lower case
        if i_lower in dic_char:
            dic_char[i_lower] = dic_char.get(i_lower, 1) + 1 # Preenche o dicionário com a chave e o valor incrementado, caso não exista ainda essa chave ela recebe o valor default 1
        else:
            dic_char[i_lower] = 1
    return dic_char

           
def get_dict_list(dic): # função que ordena em ordem decrescente do número de vezes que o character aparece no livro em uma lista
    dic_list = []

    for chave in dic:
        dic_aux = {}
        value = dic[chave]
        dic_aux[chave] = value
        dic_list.append(dic_aux)

    sorted_items = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]) , reverse = True)

    return sorted_items

def print_report(sorted_items,file_contents): # função que imprime o relatório final com todos os caracteres em ordem decrescente de quantidade e o número total de palavras
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words(file_contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_items:
        if item[0].isalpha() == True:
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")  






    
    
