import os
import glob

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


def read_files_tim(dir_name, file_tim_name):
    """Чтение данных из файла *.tim."""
    file_way = f'{dir_name}\\{file_tim_name}'
    # f = open(file_way, 'r')
    try:
        file_open_name = open(file_way, 'r')
        # data_byte = file_open_name.read(4)
        # print(f'Первые 4 байта {data_byte} файла')
        with open(file_way, 'r') as fh:
            content = fh.read()
        print("Print the full content of the binary file:")
        print(content)
    except FileExistsError:
        print('Ошибка открытия файла.')
    finally:
        file_open_name.close()
    # return result


def read_files_ofs(file_ofs_name):
    """Чтение данных из файла *.ofs."""
    pass


def read_files_dat(file_dat_name):
    """Чтение данных из файла *.dat."""
    pass


def read_files_crc(file_crc_name):
    """Чтение данных из файла *.crc."""
    pass

    """
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
    # file_name = 'Par00.tim'
    print(read_files_tim(FILE_BIN_DIR_NAME, 'Par00.tim'))


if __name__ == '__main__':
    main()
