import read_csv_file
import input_data
import time


def main():
    """Основная программа."""
    start_time = time.time()
    file_dir = input_data.read_dir()
    file_source = input_data.read_file_name_source()
    file_receiver = input_data.read_file_name_receiver()
    date_time_run = input_data.put_date_time_run()
    date_time_end = input_data.put_date_time_end()
    file_source_normal = file_receiver
    file_receiver_normal = file_receiver[
        0:len(file_receiver)-4] + '7' + '.txt'
    read_csv_file.create_parse_file(file_dir, file_source, file_receiver)
    data_source_file = read_csv_file.create_normal_file(
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
    work_time = time.time() - start_time
    print(f'Время выполнения программы - {work_time} секунды')


if __name__ == '__main__':
    main()
