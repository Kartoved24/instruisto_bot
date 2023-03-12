import json
# импортируем список слов из общего неизменяемого списка слов в личный изменяемый список слов
try:
    with open('list_of_unstudied.txt') as file_of_unstudied:
        list_of_unstudied = file_of_unstudied.read()
except:
    with open('start_list.txt', 'w') as start_list:
        list_of_unstudied = start_list.read()
        with open('list_of_unstudied', 'w') as file_of_unstudied:
            file_of_unstudied.write(list_of_unstudied)


def add_to_studied_words(new_word):
    with open('list_of_studied_words.txt', 'a') as file_of_studied:
        print(new_word, file=file_of_studied)


def delete_word_from_unstudied():
    with open('list_of_unstudied.txt', 'w') as file_of_unstudied:
        print(list_of_unstudied, file=file_of_unstudied)
