import os
import json

# грузим  json
def load_data(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return json.load(file)

# сохраняем в json
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# выводим страницами
def display_records(records, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    for index, record in enumerate(records[start_index:end_index], start=start_index + 1):
        print(f"{index}. {record}")

# добавляем запись 
def add_record(data):
    record = {}
    for field in ["фамилия", "имя", "отчество", "название организации", "телефон рабочий", "телефон личный"]:
        record[field] = input(f"Введите {field}: ")
    data.append(record)
    print("Запись успешно добавлена!")
    save_data(data, "phonebook.json") 

# редактируем запись
def edit_record(data):
    index = int(input("Введите номер записи для редактирования: ")) - 1
    if 0 <= index < len(data):
        record = data[index]
        field = input("Введите поле для редактирования: ")
        if field in record:
            record[field] = input(f"Введите новое значение для {field}: ")
            print("Запись успешно отредактирована!")
        else:
            print("Указанное поле не найдено!")
    else:
        print("Неверный номер записи!")

# поиск записи
# поиск записей по характеристикам
def search_records(data):
    criteria = input("Введите характеристики для поиска (через запятую): ").split(",")
    query = [c.strip().lower() for c in criteria]
    results = []

    for record in data:
        match = True
        for q in query:
            found = False
            for value in record.values():
                if q in str(value).lower():
                    found = True
                    break
            if not found:
                match = False
                break
        if match:
            results.append(record)

    if results:
        print("Результаты поиска:")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result}")
    else:
        print("По вашему запросу ничего не найдено.")

# загружаем данные из файла JSON
def load_custom_file():
    while True:
        file_name = input("Введите имя файла для загрузки данных: ")
        if not file_name.endswith(".json"):
            file_name += ".json"
        if os.path.exists(file_name):
            data = load_data(file_name)
            print(f"База данных с '{file_name}' успешно загружена!")
            return data
        else:
            print("Указанный файл не существует.")

# Основная функция
def main():
    file_name = "phonebook.json"
    page_size = 5
    data = load_data(file_name)

    while True:
        print("\nМеню:")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Загрузка файла JSON")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            page_number = 1
            while True:
                display_records(data, page_size, page_number)
                command = input("Нажмите '>' для следующей страницы, '<' для предыдущей, или 'q' для выхода: ")
                if command == ">":
                    page_number += 1
                elif command == "<" and page_number > 1:
                    page_number -= 1
                elif command == "q":
                    break
                else:
                    print("Не правильная команда!")
        
        elif choice == "2":
            add_record(data)
        
        elif choice == "3":
            edit_record(data)
        
        elif choice == "4":
            search_records(data)
        
        elif choice == "5":
            data = load_custom_file()
        
        elif choice == "6":
            save_data(data, file_name)
            print("👋")
            break
        
        else:
            print("Некорректный ввод!")

if __name__ == "__main__":
    main()
