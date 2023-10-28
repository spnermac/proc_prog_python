# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(str1,str2, sign):
    str1 = set(str1.split(sign))
    str2 = str2.split(sign)
    common = str1.intersection(str2)
    return  sorted(list(common))
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group, '|'))


