import datetime
# import input_data


def get_data_from_file(
        left_edge, right_edge, file_data_name,
        flag_record, time_start_date, fag_file):
    # flag_record - 0 или 1,
    # 0 - заполняем нулями, 1 - записываем данные из файла
    # fag_file - 0 или 1,
    # 0 - это исходный файл от НИКИЭТ, 1 - уже нормализованный нами файл
    result_temp_str = ''
    # Получим данные из файла ранее указанным именем
    for count in range(left_edge, right_edge):
        test = str(file_data_name[count])
        # Преобразование к формату дата время, возможно неактуально
        # date_time_event = datetime.datetime.strptime(
        #     test[2:12] + ' ' + test[13:21], '%d.%m.%Y %H:%M:%S')
        # Просто вытащим из файла дату и время без преобразований
        if flag_record == 1:
            if fag_file == 0:
                date_time_event = test[2:12] + ' ' + test[13:21]
                if int(test[28:30]) < 10:
                    data_event = 0
                else:
                    data_event = int(test[28:len(test) - 1])
                result_temp_str = (result_temp_str + date_time_event
                                   + '\t' + str(data_event) + '\n')
            elif fag_file == 1:
                date_time_event = datetime.datetime.strptime(
                    test[0:19], '%d.%m.%Y %H:%M:%S')
                data_event = int(test[20:len(test) - 1])
                result_temp_str = (result_temp_str + str(date_time_event)
                                   + '\t' + str(data_event) + '\n')
        else:
            result_temp_str = (
                    result_temp_str + str(time_start_date)
                    + '\t' + '0.0000' + '\n')
            time_start_date = (time_start_date
                               + datetime.timedelta(seconds=1))
    # result = result_temp_str
    return result_temp_str


def read_files_txt_scalar(dir_name, file_name):
    """Построчное чтение данных из файла csv с разбивкой на поля."""
    file_dir_name = dir_name
    file_csv_name = file_name
    file_way = f'{file_dir_name}\\{file_csv_name}'
    print(file_way)
    f = open(file_way, 'r')
    try:
        temp_file_content = f.readlines()
        result = get_data_from_file(
            0, len(temp_file_content), temp_file_content, 1, 0, 0)
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


def search_for_right_and_left_borders(
        file_receiver_normal, date_time_run, date_time_end):
    # Флаги правой и левой границ (flag_right_event, flag_left_event),
    # нужны для однократного (однозначного) определения номера строки в файле
    flag_right_event = 0
    flag_left_event = 0
    result_arr = []
    # Прочитаем последовательно дату и время
    # из уже открытого нормализованного файла
    for count in range(0, len(file_receiver_normal)):
        test = str(file_receiver_normal[count])
        date_time_event = datetime.datetime.strptime(
            test[0:19], '%d.%m.%Y %H:%M:%S')
        if date_time_event >= date_time_run and flag_right_event == 0:
            result = result_arr.append(count)
            flag_right_event = 1
        if date_time_event >= date_time_end and flag_left_event == 0:
            result = result_arr.append(count)
            flag_left_event = 1
            break
    result = result_arr
    return result
    # print(result)


def create_normal_file(
        file_name_source_normal, file_receiver_normal,
        date_time_run, date_time_end, dir_name):
    # date_time_run_as_date - время с которого необходимо создать файл
    print(f'Имя файла источника для нормализации - {file_name_source_normal}')
    print(f'Имя файла приемника с нормализацией - {file_receiver_normal}')
    date_time_run_as_date = datetime.datetime.strptime(
        date_time_run, '%d.%m.%Y %H:%M:%S')
    date_time_end_as_date = datetime.datetime.strptime(
        date_time_end, '%d.%m.%Y %H:%M:%S')
    print(f'Время начала файла для нас - {date_time_run_as_date}')
    print(f'Время конца файла для нас - {date_time_end_as_date}')
    file_way_source = f'{dir_name}\\{file_name_source_normal}'
    f = open(file_way_source, 'r')
    try:
        temp_file_content = f.readlines()
        # result_temp_str = ''
        # Сравним начала файлов и их конец
        date_time_event = temp_file_content[0]
        date_time_event_run = datetime.datetime.strptime(
                date_time_event[0:19], '%d.%m.%Y %H:%M:%S'
                )
        date_time_event = temp_file_content[len(temp_file_content)-1]
        date_time_event_end = datetime.datetime.strptime(
                date_time_event[0:19], '%d.%m.%Y %H:%M:%S'
                )
        right_edge_left = int((date_time_event_run
                               - date_time_run_as_date).total_seconds())
        right_edge_right = int((date_time_end_as_date
                                - date_time_event_end).total_seconds())
        # Опишем случаи
        # 1. Нули, файл, нули
        if (date_time_event_run > date_time_run_as_date
           and date_time_event_end < date_time_end_as_date):
            # variant = 1
            """
            right_edge_left = int((date_time_event_run
                                   - date_time_run_as_date).total_seconds())
            right_edge_right = int((date_time_end_as_date
                                    - date_time_event_end).total_seconds())
            """
            result_left = get_data_from_file(
                0, right_edge_left, temp_file_content,
                0, date_time_run_as_date, 1)
            result_middle = get_data_from_file(
                0, len(temp_file_content), temp_file_content, 1, 0, 1)
            result_right = get_data_from_file(
                0, right_edge_right, temp_file_content,
                0, date_time_event_end + datetime.timedelta(seconds=1), 1)
            result = result_left + result_middle + result_right
        # 2. Обрезка файла, файл, обрезка файла
        elif (date_time_event_run < date_time_run_as_date
              and date_time_event_end > date_time_end_as_date):
            # variant = 2
            # Необходимо расчитать правую и левую границы файла
            borders_arr = search_for_right_and_left_borders(
                temp_file_content, date_time_run_as_date,
                date_time_end_as_date)
            left_edge = borders_arr[0]
            right_edge = borders_arr[1]
            result_middle = get_data_from_file(
                left_edge, right_edge, temp_file_content, 1, 0, 1)
            result = result_middle
        # 3. Нули, файл, обрезка файла
        elif (date_time_event_run > date_time_run_as_date
              and date_time_event_end > date_time_end_as_date):
            # variant = 3
            result_left = get_data_from_file(
                0, right_edge_left, temp_file_content,
                0, date_time_run_as_date, 1)
            # Необходимо расчитать правую границу файла
            borders_arr = search_for_right_and_left_borders(
                temp_file_content, date_time_run_as_date,
                date_time_end_as_date)
            # left_edge = borders_arr[0]
            right_edge = borders_arr[1]
            result_middle = get_data_from_file(
                0, right_edge, temp_file_content, 1, 0, 1)
            result = result_left + result_middle
        # 4. Обрезка файла, файл, нули
        elif (date_time_event_run < date_time_run_as_date
              and date_time_event_end < date_time_end_as_date):
            # variant = 4
            # Необходимо расчитать левую границу файла
            borders_arr = search_for_right_and_left_borders(
                temp_file_content, date_time_run_as_date,
                date_time_end_as_date)
            left_edge = borders_arr[0]
            # right_edge = borders_arr[1]
            result_middle = get_data_from_file(
                left_edge, len(temp_file_content), temp_file_content, 1, 0, 1)
            result_right = get_data_from_file(
                0, right_edge_right, temp_file_content,
                0, date_time_event_end + datetime.timedelta(seconds=1), 1)
            result = result_middle + result_right
        # 5. Файл (времена равны)
        elif (date_time_event_run == date_time_run_as_date
              and date_time_event_end == date_time_end_as_date):
            # variant = 5
            result = get_data_from_file(
                0, len(temp_file_content), temp_file_content, 1, 0, 1)
    finally:
        f.close()
    return result


"""
def main():
    file_dir = input_data.read_dir()
    file_source = input_data.read_file_name_source()
    file_receiver = input_data.read_file_name_receiver()
    date_time_run = input_data.put_date_time_run()
    date_time_end = input_data.put_date_time_end()
    file_source_normal = file_receiver
    file_receiver_normal = file_receiver[0:len(file_receiver)-4] + '7' + '.txt'
    create_parse_file(file_dir, file_source, file_receiver)
    data_source_file = create_normal_file(
        file_source_normal, file_receiver_normal,
        date_time_run, date_time_end, file_dir
        )
    file_way = f'{file_dir}\\{file_receiver_normal}'
    print(file_way)
    f = open(file_way, 'w')
    try:
        f.write(data_source_file)
    finally:
        f.close()


if __name__ == '__main__':
    main()
"""
