from typing import Iterable

from selenium import webdriver

from factories import build_movie_service, build_invoice_service

# Criar interface gráfica para input de query e invoices
# interface para visualizar quais dados foram inseridos no BD

def main(query: str, invoices: Iterable[int]) -> None:
    driver = webdriver.Chrome()
    movie_service = build_movie_service(driver)
    invoice_service = build_invoice_service(driver)
    try:
        movie_service.get_movies(query=query)
        invoice_service.get_invoices(invoices=invoices)

    finally:
        movie_service.repository.db.close()
        driver.quit()

if __name__ == "__main__":
    filme = "Avengers"
    invoices = (2, 4)
    main(query=filme, invoices=invoices)
