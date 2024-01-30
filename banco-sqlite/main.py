import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'CUSTOMERS'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criar tabela
cursor.execute(
    F'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Deletar tabela

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Registrar valores nas colunas da tabela
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(:name, :weight)'

)
# cursor.execute(sql, ['Mateus', 9])
# cursor.executemany(
#     sql,
#     (
#         ('Mateus', 9), ('Fernanda', 8))
# )
cursor.execute(sql, {'name': 'Mateus', 'weight': 9})
cursor.executemany(sql, (
    {'name': 'João', 'weight': 5},
    {'name': 'Pedro', 'weight': 3},
    {'name': 'Maria', 'weight': 10},
))
connection.commit()

# cursor.close()
# connection.close()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3" '
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name = "Qualquer", weight = 45.98 '
        'WHERE id = "2" '
    )
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
