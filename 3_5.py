
# 3.5


import random

def get_jokes(counter, repeats=False):

    joke_list = []

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


    '''Проверяем второй аргумент функции, если флаг ложь, мы добавляем неповторяющиеся элементы в список, а если истина,
       наоборот '''
    if not repeats:

        '''Проверяем минимальное кол-во трёх списков на кол-во текста: если кол-во текста больше минимума длины трёх
         списков, возращаем None '''
        if count > min(len(nouns), len(adverbs), len(adjectives)):
            print(None)

        else:
            random.shuffle(nouns)  # перемешиваем изменяемую последовательность на месте
            random.shuffle(adverbs)
            random.shuffle(adjectives)

            for i in range(count):
                joke_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(count):
            noun = random.choice(nouns)      # берем один случайный элемент из списка
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)

            joke_list.append(f'{noun} {adverb} {adjective}')

    print(joke_list)

count = int(input())

get_jokes(count)



