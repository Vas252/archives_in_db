import os
# simport string
import datetime

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
    print('Введите имя файла результата поиска в формате CS009_21.txt')
    # Файл будет создан или перезаписан, проверка не требуется
    # file_name_source = input()
    file_name_receiver = 'CS009_21.txt'
    return file_name_receiver


def put_date_time_run():
    # Запросим у пользователя время начала для файла
    print('Введите дату/время начала в формате ДД.ММ.ГГ чч:мм:сс')
    # date_time_run = input()
    date_time_run = '23.08.2023 10:38:04'
    return date_time_run


def put_date_time_end():
    # Запросим у пользователя время конца для файла
    print('Введите дату/время конца файла в формате ДД.ММ.ГГ чч:мм:сс')
    # date_time_end = input()
    date_time_end = '23.08.2023 14:36:27'
    return date_time_end


def read_files_txt_scalar(dir_name, file_name):
    """Построчное чтение данных из файла csv с разбивкой на поля."""
    # result = []
    file_dir_name = dir_name
    file_csv_name = file_name
    file_way = f'{file_dir_name}\\{file_csv_name}'
    print(file_way)
    f = open(file_way, 'r')
    try:
        temp_file_content = f.readlines()
        result_temp_str = ''
        # Получим данные из файла ранее указанным именем
        for count in range(0, len(temp_file_content)):
            test = str(temp_file_content[count])
            # Преобразование к формату дата время, возможно неактуально
            # date_time_event = datetime.datetime.strptime(
            #     test[2:12] + ' ' + test[13:21], '%d.%m.%Y %H:%M:%S')
            # Просто вытащим из файла дату и время юез преобразований
            date_time_event = test[2:12] + ' ' + test[13:21]
            if int(test[28:30]) < 10:
                data_event = 0
            else:
                data_event = int(test[28:len(test) - 1])
            result_temp_str = (result_temp_str + date_time_event
                               + '\t' + str(data_event) + '\n')
        result = result_temp_str
    finally:
        f.close()
    return result


def create_parse_file(file_dir, file_name_source, file_name_receiver):
    file_dir_name = file_dir
    data_source_file = read_files_txt_scalar(file_dir_name, file_name_source)
    file_way = f'{file_dir_name}\\{file_name_receiver}'
    print(file_way)
    f = open(file_way, 'w')
    try:
        f.write(data_source_file)
    finally:
        f.close()


def create_normal_file(
        file_name_source_normal, file_receiver_normal,
        date_time_run, date_time_end, dir_name):
    print(f'Имя файла источника для нормализации - {file_name_source_normal}')
    print(f'Имя файла приемника с нормализацией - {file_receiver_normal}')
    date_time_run_as_date = datetime.datetime.strptime(
        date_time_run, '%d.%m.%Y %H:%M:%S')
    date_time_end_as_date = datetime.datetime.strptime(
        date_time_end, '%d.%m.%Y %H:%M:%S')
    print(f'Время начала файла - {date_time_run_as_date}')
    print(f'Время конца файла - {date_time_end_as_date}')


def main():
    file_dir = read_dir()
    file_source = read_file_name_source()
    file_receiver = read_file_name_receiver()
    date_time_run = put_date_time_run()
    date_time_end = put_date_time_end()
    file_source_normal = file_receiver
    file_receiver_normal = file_receiver[0:len(file_receiver)-4] + '7' + '.txt'
    create_parse_file(file_dir, file_source, file_receiver)
    create_normal_file(
        file_source_normal, file_receiver_normal,
        date_time_run, date_time_end, file_dir
        )


if __name__ == '__main__':
    main()
