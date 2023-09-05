import os

from dotenv import load_dotenv

load_dotenv()

FILE_CSV_DIR_NAME = os.getenv('FILE_CSV_DIR_NAME')


def read_dir():
    """Получим имя директории и проверим ее существование."""
    print('Введите имя директории с текстовым файлом'
          + ' в формате D:\\Work\\1720'
          )
    # Надоело руками набирать)))
    # file_dir_name = input()
    file_dir_name = FILE_CSV_DIR_NAME
    # Проверим существование директории
    isExist = os.path.exists(file_dir_name)
    if isExist is True:
        # file_name_source = read_file_name_source()
        # file_dir_way = f'{file_dir_name}\\{file_name_source}'
        return file_dir_name
    else:
        # Если ее нет, то программа сломается. Обработчик ошибки дописать
        print('Такой директории не существует!!!')


def read_file_name_source():
    # Запросим у пользователя имя файла
    print('Введите имя файла исходника в формате CS009_2.txt')
    # file_name_source = input()
    # Необходимо написать проверку существования файла
    file_name_source = 'CS009_2.txt'
    return file_name_source


def read_file_name_receiver():
    # Запросим у пользователя имя файла
    print('Введите имя файла результата поиска данных в формате CS009_21.txt')
    # Файл будет создан или перезаписан, проверка не требуется
    # file_name_receiver = input()
    file_name_receiver = 'CS009_21.txt'
    return file_name_receiver


def put_date_time_run():
    # Запросим у пользователя время начала для файла
    print('Введите дату/время начала в формате ДД.ММ.ГГ чч:мм:сс')
    # date_time_run = input()
    date_time_run = '23.08.2023 10:20:21'
    return date_time_run


def put_date_time_end():
    # Запросим у пользователя время конца для файла
    print('Введите дату/время конца файла в формате ДД.ММ.ГГ чч:мм:сс')
    # date_time_end = input()
    date_time_end = '23.08.2023 14:25:27'
    return date_time_end
