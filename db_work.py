"""
В данном модуле создается соединение с сервером БД.
Далее создаются две таблицы (если не созданы ранее) и таблица (catalog)
заполняется из приложенного csv файла.
Вторая таблица с данными является связанной и заполняется данными
их файлов (txt либо bin).
"""
import os
import psycopg2
import time
from psycopg2 import OperationalError

from dotenv import load_dotenv
import read_csv_file

load_dotenv()

SERVER_NAME = os.getenv('Server_Name')
TEST_DB_NAME = os.getenv('Test_DB_Name')
DB_USER = os.getenv('DB_User_Name')
DB_PASS = os.getenv('DB_Pass')
DB_HOST = os.getenv('DB_Host')
DB_PORT = os.getenv('DB_Post')


def create_connection(
        server_name, db_user, db_password, db_host, db_port
        ):
    # Модуль подключения к БД и отключения от нее!
    connection = None
    try:
        connection = psycopg2.connect(
            database=SERVER_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
        )

        cur = connection.cursor()
        print('Соединение с базой данных успешно установлено!')

        create_base_table(cur, 'public')
        if table_data_exists(cur, 'catalog') is False:
            pass
        else:
            pass

        connection.commit()

        cur.close()
        connection.close()
    except OperationalError as e:
        print(f'Ошибка {e} при работе с базой данных')
    return connection


def checking_availability_base_table(cur, schema, table_name):
    """Проверяем наличие таблиц."""
    public = f"'{schema}'"
    work_data = f"'{table_name}'"
    request_str = f'SELECT EXISTS (SELECT 1 AS result' \
        f' FROM pg_tables WHERE schemaname = {public}' \
        f' AND tablename = {work_data});'
    cur.execute(request_str)
    tableExists = cur.fetchone()[0]
    return tableExists


def create_base_table(cur, schema):
    """
    Проверяем наличие таблиц, если их не, то создаем.
    catalog - урезанная версия каталога СТД-2.
    numbers - таблица непосредственно с данными.
    """
    table_name = 'catalog'
    tablecatalogispresent = checking_availability_base_table(
        cur, schema, table_name)

    if tablecatalogispresent is False:
        cur.execute('''CREATE TABLE CATALOG
        (id_catalog SERIAL PRIMARY KEY,
        KKS varchar(20) NOT NULL,
        KKS_discript varchar(100),
        KKS_file_name varchar(15) NOT NULL);''')
        print(f'Создали таблицу {table_name}!')
    else:
        print(f'Таблица {table_name} уже создана!')

    table_name = 'numbers'
    tablecatalogispresent = checking_availability_base_table(
        cur, schema, table_name)

    if tablecatalogispresent is False:
        cur.execute('''CREATE TABLE Numbers
        (id_numbers SERIAL PRIMARY KEY,
        KKS_num int NOT NULL,
        Date_time_val timestamp,
        Val float,
        Quality bit,
        FOREIGN KEY (KKS_num) REFERENCES Catalog (id_catalog));''')
        print(f'Создали таблицу {table_name}!')
    else:
        print(f'Таблица {table_name} уже создана!')


def table_data_exists(cur, table_name):
    """Проверка таблицы на наличие данных."""
    query = f'SELECT * FROM {table_name}'
    cur.execute(query)
    if cur.fetchone() is not None:
        print(f'Таблица {table_name} уже заполнена.')
        return True
    else:
        print(f'Таблица {table_name} не заполнена.')
        cur.execute('''COPY catalog FROM 'D:\\Work\\kks_4.csv' DELIMITER ',' CSV HEADER;''')
        return False


def create_base_and_add_data(cur, schema, db_name, arr_data):
    """Модуль создания таблицы с данными и добавления данных в неё."""
    # data_to_table = ''
    # count_in_to_table = 0

    """
    if tableExists is True:
        # print('Таблица создана ранее! Можно добавлять в нее данные!')
        for count in range(0, len(arr_data)):
            test_arr = arr_data[count]
            for i in range(0, len(test_arr)):
                test_arr_1 = test_arr[i]
                kks_val = 1
                date_val = datetime.datetime.strptime(
                    str(test_arr_1[1]), '%d.%m.%Y').date()
                time_val = test_arr_1[2]
                date_time_val = f"'{date_val} {time_val}'"
                data = test_arr_1[3]

                if count_in_to_table < 1000:
                    data_to_table = data_to_table
                    + f'({kks_val}, {date_time_val}, {data}), '
                    count_in_to_table += 1
                elif count_in_to_table == 1000:
                    data_to_table = data_to_table
                    + f'({kks_val}, {date_time_val}, {data})'
                    data_str = f'INSERT INTO WORK_DATA (KKS, DATE_TIME_VAL,' \
                        f' DATA) VALUES {data_to_table}'
                    cur.execute(data_str)
                    data_to_table = ''
                    count_in_to_table = 0
    """


def main():
    """Основная программа."""
    # data_to_table = ''
    start_time = time.time()
    create_connection(
        SERVER_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT
        )
    read_csv_file.main()

    work_time = time.time() - start_time
    print(f'Время выполнения программы - {work_time} секунды')


if __name__ == '__main__':
    main()
