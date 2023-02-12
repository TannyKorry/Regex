from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", 'r', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows) # дает список списков из файла
    # print(contacts_list)

# 1
def arrange(contacts):
    for c in contacts:
        item = ' '.join(c[:3]).split(' ')
        c[:3] = item[:3]
    return contacts

#

# 2
def format_num(contacts):
    for contact in arrange(contacts):
        pattern = r'(\+7|8)\s*\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})\s*\(?([д][о]?[б]?[.]?\s*\d+)?\)?'
        substitution = r'+7(\2)\3-\4-\5 \6'
        res = re.sub(pattern, substitution, contact[5])
        contact[5] = res
    contacts_list.append(contact)
    return contacts_list

# 3
def remove_duplicates(contacts):
    item_set = []
    shablon = ''
    print(f"функция\n "
           f"{format_num(contacts)}\n")
    for item in format_num(contacts)[0::]:
        print(f'item: {item}')
        shablon = item[0].split(',')[0]
        print(f'шаблон: {shablon}\n')
        for itm in format_num(contacts)[0::]:
            print(f'\nitm: {itm}\n')
            print(f"itm[0].split(',')[0]: {itm[0].split(', ')[0]} равен {shablon}?")
            if itm[0].split(',')[0] == shablon:
                item_set += itm
                pprint(f'item_set: {item_set}')
            else:
                pass


#
# TODO 1: выполните пункты 1-3 ДЗ
# pattern = re.compile('(\+7|8).?\(?\d+\)?.\d+.?\d+.?\d+\s?\(?[д]?[о]?[б]?.?\s?\d+\)?')
# result = pattern.findall(contacts_list)
# print(result)
# TODO 2: сохраните получившиеся данные в другой файл
    def save_pc(self):
        """Функция скачивает контент на комп в папку BACKUP"""
        # os.mkdir('BACKUP')
        # print('Создание папки BACKUP для резервного копирования на компьютере')
        # path = os.path.join(os.getcwd(), 'Regex')
        #
        # for name, props in :
        #     full_path = os.path.join(path, 'phonebook.csv')
        #     # ph = requests.get(props[-1])
        #     out = open(full_path, "wb")
        #     out.write(ph.content)
        #     out.close()
        # return

# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)


if __name__ == '__main__':
    # print(arrange(contacts_list))
    print(format_num(contacts_list))
    print('\n')
    # remove_duplicates(contacts_list)

