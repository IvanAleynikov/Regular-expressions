from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

import re

# TODO 1: выполните пункты 1-3 ДЗ
name_list = []
paramerts = contacts_list.pop(0)

for name in contacts_list:
  name_lname = ' '.join(name[0:3])
  name_lname_correct = r"([А-Яёа-я]+)\s([А-Яёа-я]+)\s([А-Яёа-я]*)(\s*)"
  new_name = r"\1, \2, \3"
  res_name = re.sub(name_lname_correct, new_name, name_lname)

  number_sec_correct = r"[\s(]*(\D+)\.\s(\d+)[\s)]*"
  new_number_sec = r" \1.\2"
  res_num_sec = re.sub(number_sec_correct, new_number_sec, name[-2])
  name[-2] = res_num_sec

  number_correct = r"(\+7|8)\s*[\s(]*(\d+)[\s)]*[\s-]*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
  new_number = r"+7(\2)\3-\4-\5"
  res_number = re.sub(number_correct, new_number, name[-2])
  name[-2] = res_number

  name_list.append(res_name.split(', ') + name[3:])

merged_data = []
seen_names = set()

for person_data in name_list:
    full_name = f"{person_data[0]} {person_data[1]}"

    if full_name not in seen_names:
        seen_names.add(full_name)
        merged_data.append(person_data)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(merged_data)
pprint(merged_data)