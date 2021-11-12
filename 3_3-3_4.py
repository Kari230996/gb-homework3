# 3.3-3.4

#3.3

# def thesaurus(*names):
#     new_dir = {}
#
#     for name in names:
#         new_dir.setdefault(name[0], [])
#         new_dir[name[0]].append(name)
#     print(new_dir)
#
# thesaurus("Мария", "Петр", "Илья", "Агата", "Мелисса",'Иван')


#3.4

def thesaurus(*names_surnames):
    new_dict = {}

    for name_surname in names_surnames:
        name, surname = name_surname.split()
        new_dict.setdefault(surname[0], {})
        new_dict[surname[0]].setdefault(name[0], [])
        new_dict[surname[0]][name[0]].append(name_surname)

    print(new_dict)

thesaurus('Петр Алексеев', 'Мария Аленова', 'Карина Апаева', 'Агата Кристи', 'Мелисса Фаллетта', 'Иван Сергеев')









