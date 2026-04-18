import mysql.connector

from utils.db_utils import db_insert, db_get_all


class MovieRepository:
    """Interface de acesso ao BD para a entidade Movie"""

    def __init__(self, db: mysql.connector.pooling.PooledMySQLConnection) -> None:
        self.db = db

    def insert(
        self,
        title: str,
        description: str,
    ) -> None:
        """Insere um filme e sua descrição no BD

        Args:
            title (str): título do filme
            description (str): descrição do filme
        """
        db_insert(
            db=self.db,
            table="movies",
            fields="(movie_name, description)",
            values=(title, description)
        )

    def get_all(self) -> list[tuple]:
        """Retorna todos os filmes presentes no BD"""
        return db_get_all(
            db=self.db,
            table="movies",
            fields="movie_name, description"
        )
