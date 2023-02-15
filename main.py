from pprint import pprint
import csv
import re
import os


def read(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows) # дает список списков из файла
    return contacts_list
# 1
def arrange(contacts):
    for c in contacts:
        item = ' '.join(c[:3]).split(' ')
        c[:3] = item[:3]
    return contacts

# 2
def format_num(contacts):
    contact_list = []
    for contact in arrange(contacts):
        pattern = r'(\+7|8)\s*\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})\s*\(?([д][о]?[б]?[.]?\s*\d+)?\)?'
        substitution = r'+7(\2)\3-\4-\5 \6'
        res = re.sub(pattern, substitution, contact[5])
        contact[5] = res
        contact_list.append(contact)
    return contact_list

# 3
def remove_duplicates(contacts):
    result = []
    for i, cont_1 in enumerate(format_num(contacts)):
        result.append(cont_1[:7])
        for cont_2 in format_num(contacts):
            if cont_2[0] == cont_1[0]:
                for j in range(1, 7):
                    if result[i][j] == '':
                        result[i][j] = cont_2[j]
    for x in result:
        if result.count(x) > 1:
            result.remove(x)
    return result
#

# код для записи файла в формате CSV
def recording(contacts):
    path = os.path.join(os.getcwd())
    full_path = os.path.join(path, 'phonebook.csv')
    with open(full_path, "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      datawriter.writerows(contacts)


if __name__ == '__main__':
    # Задание1
    # pprint(arrange(read("phonebook_raw.csv")))

    # Задание2
    # pprint(format_num(read("phonebook_raw.csv")))

    # Задание3
    # pprint(remove_duplicates(read("phonebook_raw.csv")))
    recording(remove_duplicates(read("phonebook_raw.csv")))
