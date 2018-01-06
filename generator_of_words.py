import random

dict_of_words = {}
count_of_chance = 0
dict_of_chance = {}
word_history = []
answer_history = []


def get_random_word():
    random_word = ""
    random_number = random.randrange(1, count_of_chance)
    sum_of_chance = 0
    for i in dict_of_chance:
        sum_of_chance += int(dict_of_chance[i])
        if sum_of_chance >= random_number:
            random_word = i
            break
    return random_word


def fill_words():
    global dict_of_words
    dictionary = open("dictionary", "r")
    data = dictionary.readlines()
    for i in data:
        english_word, russian_word = i.split(":")
        dict_of_words[english_word] = russian_word.strip()
        dict_of_words[russian_word.strip()] = english_word


def fill_chance():
    global dict_of_chance, count_of_chance
    dictionary = open("dict_chance", "r")
    data = dictionary.readlines()
    for i in data:
        word, chance = i.split(":")
        dict_of_chance[word] = chance.strip()
    for i in dict_of_words.keys():
        if i not in dict_of_chance.keys():
            dict_of_chance[i] = 1
    for i in dict_of_chance.values():
        count_of_chance += int(i)


def save_chance():
    file = open("dict_chance", "w")
    for i in dict_of_chance:
        file.write("{}:{}\n".format(i, dict_of_chance[i]))


def fill_history():
    global word_history, answer_history
    history = open("history", "r")
    data = history.readline().split("_")
    for i in data:
        try:
            words, answer = i.split(":")
        except ValueError:
            break
        word_history.append(words)
        answer_history.append(answer)


def save_history():
    global word_history, answer_history
    history = open("history", "w")
    print(word_history)
    print(answer_history)
    lenght = len(word_history)
    if lenght > 50:
        word_history = word_history[lenght - 50:]
        answer_history = answer_history[lenght - 50:]
    for i in range(lenght):
        history.write("{}:{}_".format(word_history[i], str(answer_history[i])))
