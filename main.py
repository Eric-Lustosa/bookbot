from stats import get_book_text #Função que lê o arquivo texto do livro e retorna em uma variável string
from stats import get_book_words #Função que imprime o número de palavras que temos no livro
from stats import get_book_char # Função que cria um dicionário com o número de cada caracter sem ordem específica
from stats import get_dict_list # Cria uma lista de dicionários de maneira ordenada decrescente por número de vezes que o caracter aparece
from stats import print_report # cria report com informações gofáveis
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        bookprint = get_book_text(filepath) #Adicionar path
        get_book_words(bookprint)

        chars = get_book_char(bookprint)

        get_dict_list(chars)
        sorted_dic = get_dict_list(chars)
        
        print_report(sorted_dic,bookprint)
        

main()