from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", 'r', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows) # дает список списков из файла
    print(contacts_list)
    print()
    print()
# 1
new_contacts_list = []
for c in contacts_list:
    if len(c[0].split()) == 1: # Если фамилия есть и не содержит больше ничего, кроме себя.
        element = [c[0] + ', ' + c[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
    elif len(c[0].split()) > 1: # Если в фамилию вбито что-то помимо фамилии
        s = c[0].split()
        if len(c[0].split()) == 2:  # Если фамилия содержит фамилию и имя
            element = [s[0] + ', ' + s[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        else: # Если фамилия содержит фамилию, имя и отчество
            element = [s[0] + ', ' + s[1] + ', ' + s[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]

    if len(c[1].split()) == 1:  # Если в имя содержит только имя
        element = [c[0] + ', ' + c[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
    elif len(c[1].split()) > 1:# Если в имя вбито что-то помимо имени
        s = c[1].split()
        if c[0] != "": # Если фамилия есть, а в имя вбиты имя-отчество
            element = [c[0] + ', ' + s[0] + ', ' + s[1] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        elif c[2] != "": # Если фамилии нет, отчество есть, а имя содержит ФИ
            element = [s[0] + ', ' + s[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        else:
            element = [s[0] + ', ' + s[1] + ', ' + s[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
    new_contacts_list.append(element)
pprint(new_contacts_list)
# 3
if new_contacts_list[0:1]



# 2
for i in c:
    pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})\s*\(?([д][о]?[б]?[.]?\s*\d+)?\)?"
    substitution = r'+7(\2)\3-\4-\5 \6'
    result = re.findall(pattern, i)
    result = re.sub(pattern, substitution, i)

# # TODO 1: выполните пункты 1-3 ДЗ
# # pattern = re.compile('(\+7|8).?\(?\d+\)?.\d+.?\d+.?\d+\s?\(?[д]?[о]?[б]?.?\s?\d+\)?')
# # result = pattern.findall(contacts_list)
# # print(result)
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# # with open("phonebook.csv", "w") as f:
# #   datawriter = csv.writer(f, delimiter=',')
# #   # Вместо contacts_list подставьте свой список
# #   datawriter.writerows(contacts_list)
#
#
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
#     # print_hi('PyCharm')
#     # pprint(contacts_list)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# #(\+7|8).?\(?\d+\)?.\d+.?\d+.?\d+     все телефонные номера без добавочных
# #(\+7|8).?\(?\d+\)?.\d+.?\d+.?\d+\s?\(?[д]?[о]?[б]?.?\s?\d+\)?
# # '\s*(\+7|8)?\s*\(*(\d+)\)*\s*(\d+)[-\s]+(\d+)[-\s](\d+)'