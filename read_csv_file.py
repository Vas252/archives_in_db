import os

from dotenv import load_dotenv

load_dotenv()

FILE_CSV_DIR_NAME = os.getenv('FILE_CSV_DIR_NAME')


def read_dir():
    """Получим имя директории и проверим ее существование."""
    print('Введите имя директории с текстовым файлом'
          + ' для добавления данных в таблицу catalog:'
          )
    # Надоело руками набирать)))
    # file_dir_name = input()
    # file_dir_name = "D:\Work\txt_test"
    file_dir_name = FILE_CSV_DIR_NAME
    # Проверим существование директории
    isExist = os.path.exists(file_dir_name)
    if isExist is True:
        return file_dir_name
    else:
        # Если ее нет, то программа сломается. Обработчик ошибки дописать
        print('Такой директории не существует!!!')


def read_files_txt_scalar(file_csv_name):
    """Построчное чтение данных из файла csv с разбивкой на поля."""
    result = []
    file_dir_name = FILE_CSV_DIR_NAME
    # for count in list_file_txt_scalar:
    file_way = f'{file_dir_name}\\{file_csv_name}'
    print(file_way)
    f = open(file_way, 'r')
    try:
        temp_file_content = f.readlines()
        result_temp = []
        # Получим данные из файла с именем файла
        result_temp = [
            list(map(str, file_csv_name +
                     " " + (temp_file_content[i]).split()))
            # list(map(str, (temp_file_content[i]).split(',').strip()))
            for i in range(0, len(temp_file_content))
        ]
        result.append(result_temp)
    finally:
        f.close()
    return result


def main():
    work_dir = read_dir()
    print(f'Рабочая директория - {work_dir}')
    print(read_files_txt_scalar('kks.csv'))


if __name__ == '__main__':
    main()
