import os

import pymysql
import dotenv

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

TABLE_NAME = 'customers'

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}  ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )

        # LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Manipulando dados a partir daqui

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) ' 
            'VALUES ' 
            '(%s, %s) '
        )

        data = (
            ('Mateus', 24),
            ('Fernanda', 26),
        )

        cursor.executemany(sql, data)

    connection.commit()

    # Lendo valores com SELECT
    with connection.cursor() as cursor:
        menor_id = int(input('Menor id: '))
        maior_id = int(input('Maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))

        for row in cursor.fetchall():
            print(row)

        # Deletando dados do banco com DELETE
        with connection.cursor() as cursor:

            sql = (
                f'DELETE FROM {TABLE_NAME} '
                f'WHERE id = %s '
            )
            print(cursor.execute(sql, (1,)))
            connection.commit()

            cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

            for row in cursor.fetchall():
                print(row)
