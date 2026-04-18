from typing import Iterable

import mysql.connector


def db_insert(
    db: mysql.connector.pooling.PooledMySQLConnection,
    table: str,
    fields: str,
    values: Iterable[str]
) -> None:
    """Função genérica para inserção de dados no BD

    Args:
        db: Conexão com o BD
        table: Nome da tabela onde os dados serão inseridos
        fields: Campos onde os dados serão inseridos, no formato "(campo1, campo2, ...)"
        values: Valores a serem inseridos, na mesma ordem dos campos
    """
    cursor = db.cursor()

    query = f"INSERT INTO {table} {fields} VALUES ("
    for _ in values:
        query += """%s,"""
    query = query[:-1] + ")"

    cursor.execute(query, values)
    db.commit()

    cursor.close()


def db_get_all(
    db: mysql.connector.pooling.PooledMySQLConnection,
    table: str,
    fields: str
) -> list[tuple]:
    """Função genérica para obtenção de todos os dados de N colunas de uma tabela do BD

    Args:
        db: Conexão com o BD
        table: Nome da tabela de onde os dados serão obtidos
        fields: Campos a serem obtidos, no formato "campo1, campo2, ..."

    Returns:
        list[tuple]: Lista de tuplas, onde cada tupla representa uma linha da tabela
    """
    cursor = db.cursor()
    query = f"SELECT {fields} FROM {table}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
