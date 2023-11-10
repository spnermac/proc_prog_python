import json

with open('input.json', 'r') as file:
    data = json.load(file)


'''список для записи произведений'''
multi = []

# TODO решите задачу
def task() -> float:
    for i in data:
        dict_1 = dict(i)
        multi.append(dict_1['score'] * dict_1['weight'])
    return round(sum(multi), 3)

print(task())
