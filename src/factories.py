import os

from dotenv import load_dotenv
from selenium import webdriver
import mysql.connector

from repositories.movie_repository import MovieRepository
from services.invoice_service import InvoiceService
from services.movie_service import MovieService


load_dotenv()


def build_movie_service(driver: webdriver.Chrome):
    """Cria o serviço para a entidade Movie"""
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    movie_repository = MovieRepository(db=db)
    movie_service = MovieService(driver=driver, repository=movie_repository)
    return movie_service


def build_invoice_service(driver: webdriver.Chrome):
    """Cria o serviço para a entidade Invoice"""
    invoice_service = InvoiceService(driver=driver)
    return invoice_service
