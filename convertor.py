# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open("input.csv", "r") as file1:
        data_csv = csv.DictReader(file1, delimiter=',', quotechar='"')

        json_data = []
        for row in data_csv:
            json_data.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open('output.json', "w") as file2:
        json.dump(json_data, file2, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
