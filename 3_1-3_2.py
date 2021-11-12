# 3.1-3.2

def num_translate(rus_num):
    vocabulary = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}

    if rus_num[0].isupper() :
        return vocabulary[rus_num.lower()].capitalize()
    elif rus_num in vocabulary.keys():
        return vocabulary[rus_num]
    else:
        return None
while True:
    num = input("Введите числа на английском от 0 до 10 ")
    print('Перевод введенного числа: ', num_translate(num))
    print()

