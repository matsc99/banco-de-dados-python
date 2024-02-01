import os

import pymysql
import dotenv
import pymysql.cursors

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
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
            ('Marcos', 78),
            ('Giovanni', 30),
            ('Fernando', 45),
            ('Tales', 100),
            ('Luiz', 89),
        )

        cursor.executemany(sql, data)

        for row in cursor.fetchall():
            print(row)

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
            (cursor.execute(sql, (1,)))
            connection.commit()

            cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

            for row in cursor.fetchall():
                print(row)

        # Atualizando dados
        with connection.cursor() as cursor:
            sql = (
                f'UPDATE {TABLE_NAME} '
                'SET nome = %s, idade=%s '
                f'WHERE id = %s '
            )
            cursor.execute(sql, ('Mateus', 24, 2))
            connection.commit()

            cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

            for row in cursor.fetchall():
                print(row)
