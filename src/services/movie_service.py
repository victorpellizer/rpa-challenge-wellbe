from datetime import datetime
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from repositories.movie_repository import MovieRepository


class MovieService:
    """Serviço para a entidade Movie"""

    def __init__(
        self,
        driver: webdriver.Chrome,
        repository: MovieRepository
    ) -> None:
        self.driver = driver
        self.repository = repository

    def get_movies(self, query: str) -> None:
        """Lógica para extrair os filmes do site e salvar no BD

        Args:
            query: filtro para busca dos filmes
        """
        # Acessar o site
        self.driver.get("https://rpachallenge.com/")
        time.sleep(2)

        # Maximizar janela para evitar bugs de aba invisível
        self.driver.maximize_window()
        time.sleep(0.5)

        # Navegar para a aba Movie Search
        movie_tab = self.driver.find_element(By.CSS_SELECTOR, "a[href='/movieSearch']")
        movie_tab.click()
        time.sleep(2)

        # Buscar os filmes com a query desejada
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Coletar array de filmes e descrições
        movies = self.driver.find_elements(By.CSS_SELECTOR, ".cardItem")
        for movie in movies:
            try:
                title = movie.find_element(By.CSS_SELECTOR, ".card-title").text
                description = movie.find_element(By.CSS_SELECTOR,".card-reveal").find_element(By.TAG_NAME, "p").get_attribute("textContent")
                if title and description:
                    self.repository.insert(title, description)
            except Exception as e:
                print(f"Erro ao processar filme: {e}")
                continue

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        extracted_movies = self.repository.get_all()

        print("Estou aqui")
        with open("output.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["movie_name", "description"])
            for row in extracted_movies:
                writer.writerow(row)
        print("Estou aqui")
        # create_file(
        #     filename=f"movies_dump_{timestamp}.txt",
        #     content=",".join(extracted_movies)
        # )
