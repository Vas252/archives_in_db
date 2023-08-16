import os

from dotenv import load_dotenv

load_dotenv()

FILE_DIR_NAME = os.getenv('File_dir_name')


def read_dir():
    """Получим имя директории и проверим ее существование."""
    print('Введите имя директории с текстовыми файлами для обработки:')
    # Надоело руками набирать)))
    # file_dir_name = input()
    # file_dir_name = "D:\Work\txt_test"
    file_dir_name = FILE_DIR_NAME
    # Проверим существование директории
    isExist = os.path.exists(file_dir_name)
    if isExist is True:
        return file_dir_name
    else:
        # Если ее нет, то программа сломается. Обработчик ошибки дописать
        print('Такой директории не существует!!!')


def read_file_list(dir):
    """Получим имя файлов из директории и занесем их в массив."""
    list_file_txt = []
    obj = os.scandir(dir)
    for entry in obj:
        if entry.is_file() and entry.name.endswith('.txt'):
            list_file_txt.append(entry.name)
        else:
            # print(f'Выбранный каталог {dir} не содержит текстовых файлов или'
            #       f' файл {entry.name} не текстовый!')
            print(f'Файл {entry.name} не текстовый!')
    return list_file_txt


def get_list_files_vector(list_file_txt):
    """Получение списка файлов свекторными данными."""
    list_files_vector = []
    files_vector_name = ['AS01000', 'AS05000', 'ES', 'OCT_12', 'DUT']
    for count in list_file_txt:
        for count_files_vector_name in files_vector_name:
            if count_files_vector_name in count:
                list_files_vector.append(count)
    return list_files_vector


def get_list_files_scalar(list_file_txt, list_files_vector):
    """Получение списка файлов со скалярными данными."""
    list_files_scalar = list(set(list_file_txt).
                             difference(set(list_files_vector)))
    return list_files_scalar


def read_files_txt_scalar(list_file_txt_scalar):
    """Построчное чтение скалярных данных из файлов txt с разбивкой на поля."""
    result = []
    file_dir_name = FILE_DIR_NAME
    for count in list_file_txt_scalar:
        file_way = f'{file_dir_name}\\{count}'
        print(file_way)
        f = open(file_way, 'r')
        try:
            temp_file_content = f.readlines()
            result_temp = []
            # Получим данные из файла с именем файла
            result_temp = [list(map(str,
                           (
                            temp_file_content[i]).split()))
                           # (temp_file_content[i]).split()))
                           for i in range(0, len(temp_file_content))
                           ]
            result.append(result_temp)
        finally:
            f.close()
    return result


def read_files_txt_vector(list_file_txt_vektor):
    """Построчное чтение векторных данных из файлов txt с разбивкой на поля."""
    for count in list_file_txt_vektor:
        print(count)


"""
def main():
    work_dir = read_dir()
    print(f'Рабочая директория - {work_dir}')
    list_file = []
    # Проверим каталог на наличие файлов
    if len(os.listdir(work_dir)) != 0:
        print(f'Файлов в директории {len(os.listdir(work_dir))}')
        list_file = read_file_list(work_dir)
    else:
        print(f'Выбранный каталог {work_dir} не содержит файлов!')
    # Создадим список из файлов с векторными данными
    list_file_vektor = get_list_files_vector(list_file)

    # Создадим список из файлов со скалярными данными
    list_file_scalar = get_list_files_scalar(
        list_file,
        list_file_vektor
        )
    # Получим массив скалярных данных с именем файла
    file_scalar_content = read_files_txt_scalar(list_file_scalar)
    # print(f'Все данные {file_scalar_content}')
    # print(f'Элемент {file_scalar_content[0]}')
    for count_own in range(0, len(file_scalar_content)):
        test_arr = file_scalar_content[count_own]
        # print(f'Элемент эдлементов {test_arr[2]}')
        for count in range(0, len(test_arr)):
            # print(f'Мои данные count - {count}, data - {test_arr[count]}')
            test_arr_1 = test_arr[count]
            for i in range(0, len(test_arr_1)):
                print(f'Мои данные test_arr_1 , data - {test_arr_1[i]}')
        # for i in range(0, len(0, test_arr_1)):
        #     print(f'Мои данные count - {count}, i - {i},'
        #           f' data - {test_arr_1[i]}')


if __name__ == '__main__':
    main()
"""
