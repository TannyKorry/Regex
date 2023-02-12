from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", 'r', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows) # дает список списков из файла
    # print()

# 1
def arrange(contacts):
    new_contacts_list, element = [], []
    for c in contacts:
        if len(c[0].split()) == 1: # Если "lastname" есть и не содержит больше ничего.
            element = [c[0] + ', ' + c[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        elif len(c[0].split()) > 1: # Если "lastname" содержит что-то помимо фамилии.
            s = c[0].split()
            if len(c[0].split()) == 2:  # Если "lastname" содержит фамилию и имя
                element = [s[0] + ', ' + s[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
            else: # Если "lastname" содержит фамилию, имя и отчество
                element = [s[0] + ', ' + s[1] + ', ' + s[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]

        if len(c[1].split()) == 1:  # Если "firstname" содержит только имя
            element = [c[0] + ', ' + c[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        elif len(c[1].split()) > 1: # Если в "firstname" вбито что-то помимо имени:
            s = c[1].split()
            if c[0] != "": # При этом если "lastname" есть, а в "firstname" вбиты имя-отчество
                element = [c[0] + ', ' + s[0] + ', ' + s[1] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
            elif c[2] != "": # Или "lastname" нет, "surname" есть, а имя содержит фамилия-имя
                element = [s[0] + ', ' + s[1] + ', ' + c[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
            else:
                element = [s[0] + ', ' + s[1] + ', ' + s[2] + ', ' + c[3] + ', ' + c[4] + ', ' + c[5] + ', ' + c[6]]
        new_contacts_list.append(element)
    return new_contacts_list


def _split_list(L, n):
    '''
    Генератор для формирования списка списков из списка строк
    '''
    for i in range(0, len(L), n):
        yield L[i:i+n]

# 2
def format_num(contacts):
    result, cont_list, res = [], [], ''
    for contact in arrange(contacts):
        for item in contact:
            pattern = r'(\+7|8)\s*\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})\s*\(?([д][о]?[б]?[.]?\s*\d+)?\)?'
            substitution = r'+7(\2)\3-\4-\5 \6'
            res = re.sub(pattern, substitution, item)
        result.append(res)
           # Формируем список списков
    gen = _split_list(result, 1)
    for item in gen:
        cont_list.append(item)
    return cont_list

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
                if shablon in item_set:
                    print('уже есть')
                else:
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
    # pprint(arrange(contacts_list))
    # pprint(format_num(contacts_list))
    print('\n')
    remove_duplicates(contacts_list)

