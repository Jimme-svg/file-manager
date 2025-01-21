# Создаем пустой список
my_list = []

while True:
    # Выводим меню
    print("\nВыберите действие:")
    print("1. Добавить слово в список")
    print("2. Удалить слово из списка")
    print("3. Просмотреть список")
    
    choice = input("Введите номер действия (или 'stop' для выхода): ")
    
    # Проверяем хочет ли пользователь выйти
    if choice.lower() == 'stop':
        print("Программа завершена.")
        break
    
    # Обрабатываеь выбор пользователя
    elif choice == '1':
        word = input("Введите слово для добавления: ")
        my_list.append(word)
        print(f"Слово '{word}' добавлено в список.")
        
    elif choice == '2':
        if len(my_list) == 0:
            print("Список пуст!")
        else:
            word = input("Введите слово для удаления: ")
            if word in my_list:
                my_list.remove(word)
                print(f"Слово '{word}' удалено из списка.")
            else:
                print("Такого слова нет в списке!")
                
    elif choice == '3':
        if len(my_list) == 0:
            print("Список пуст!")
        else:
            print("Текущий список:")
            for i, word in enumerate(my_list, 1):
                print(f"{i}. {word}")
                
    else:
        print("Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")
 # Если нужно что то подредачить говорите, а так задание готово
