import os
import glob

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

FILE_BIN_DIR_NAME = os.getenv('FILE_BIN_DIR_NAME')


def read_dir():
    """Получим имя директории и проверим ее существование."""
    print('Введите имя директории с бинарными файлами:')
    # Надоело руками набирать)))
    # file_dir_name = input()
    # Имя тестовой директории с бинарными файлами 'D:\Work\4\'
    file_dir_name = FILE_BIN_DIR_NAME
    # Проверим существование директории
    isExist = os.path.exists(file_dir_name)
    if isExist is True:
        return file_dir_name
    else:
        # Если ее нет, то программа сломается. Обработчик ошибки дописать
        print('Такой директории не существует!!!')


def checking_all_files_in_dir(dir_name):
    """
    Проверяем наличие всех необходимых файлрв для обработки.
    Список ParXX.tim, ParXX.ofs, ParXX.dat, ParXX.crc.
    Если чего то нет, пишем в консоль и выдаем ошибку.
    """
    quantity_file_tim = len(glob.glob1(dir_name, '*.tim'))
    quantity_file_ofs = len(glob.glob1(dir_name, '*.ofs'))
    quantity_file_dat = len(glob.glob1(dir_name, '*.dat'))
    quantity_file_crc = len(glob.glob1(dir_name, '*.crc'))

    try:
        if (quantity_file_tim == quantity_file_ofs == quantity_file_dat ==
           quantity_file_crc):
            return True
        else:
            raise Exception('not all file in dir')
    except Exception:
        print(
            'В директории присутсвуют не все файлы. Обрабатывать пока не будем'
            )
        return False
    """
    quantity_file_in_dir = len(os.listdir(dir_name))
    # Создадим пустой массив для храниения номеров параметров
    num_file_array = []
    # Просмотрим все файлы и занесем номера в массив
    for file_name in os.listdir(dir_name):
        file_in_dir = os.path.join(dir_name, file_name)
        if os.path.isfile(file_in_dir):
            # print(file_name)
            pass
    # print(quantity_file_tim)
    # expansion расширение для файла
    # return os.listdir(dir_name)
    return num_file_array
    """


"""
def read_files_txt_scalar(file_csv_name):
    # Построчное чтение данных из файла csv с разбивкой на поля.
    result = []
    file_dir_name = FILE_BIN_DIR_NAME
    # for count in list_file_txt_scalar:
    file_way = f'{file_dir_name}\\{file_csv_name}'
    print(f'Список файлов в рабочей директории - {file_way}')
    f = open(file_way, 'r')
    try:
        temp_file_content = f.readlines()
        result_temp = []
        # Получим данные из файла с именем файла
        result_temp = temp_file_content
        # result_temp = [list(map(str, file_csv_name + " " + (temp_file_content[i]).split())) for i in range(0, len(temp_file_content))]
            # list(map(str, (temp_file_content[i]).split(',').strip()))
            # for i in range(0, len(temp_file_content))
        # ]
        result.append(result_temp)
    finally:
        f.close()
    return result
"""


def main():
    work_dir = read_dir()
    print(f'Рабочая директория - {work_dir}')
    if checking_all_files_in_dir(FILE_BIN_DIR_NAME) is True:
        print('В директории все файлы. Работаем дальше!')


if __name__ == '__main__':
    main()
