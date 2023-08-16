import os
import read_file
import db_work
import time

from dotenv import load_dotenv

load_dotenv()

SERVER_NAME = os.getenv('Server_Name')
TEST_DB_NAME = os.getenv('Test_DB_Name')
DB_USER = os.getenv('DB_User_Name')
DB_PASS = os.getenv('DB_Pass')
DB_HOST = os.getenv('DB_Host')
DB_PORT = os.getenv('DB_Post')


def main():
    """Основная программа."""
    start_time = time.time()
    work_dir = read_file.read_dir()
    print(f'Рабочая директория - {work_dir}')
    list_file = []
    # Проверим каталог на наличие файлов
    if len(os.listdir(work_dir)) != 0:
        print(f'Файлов в директории {len(os.listdir(work_dir))}')
        list_file = read_file.read_file_list(work_dir)
    else:
        print(f'Выбранный каталог {work_dir} не содержит файлов!')
    # Создадим список из файлов с векторными данными
    list_file_vektor = read_file.get_list_files_vector(list_file)

    # Создадим список из файлов со скалярными данными
    list_file_scalar = read_file.get_list_files_scalar(
        list_file,
        list_file_vektor
        )
    # Получим массив скалярных данных с именем файла
    file_scalar_content = read_file.read_files_txt_scalar(list_file_scalar)

    db_work.create_connection(
        SERVER_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT, TEST_DB_NAME,
        file_scalar_content
        )
    work_time = time.time() - start_time
    print(f'Время выполнения программы - {work_time} секунды')


if __name__ == '__main__':
    main()
