from datetime import datetime
from typing import Iterable
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.file_utils import download_file, zip_files


class InvoiceService:
    """Serviço para a entidade Invoice"""

    def __init__(
        self,
        driver: webdriver.Chrome,
    ) -> None:
        self.driver = driver

    def get_invoices(self, invoices: Iterable[int]) -> None:
        """Lógica para baixar invoices e salvar em um zip

        Args:
            invoices: lista de números de invoices a serem baixados
        """
        # Acessar o site
        self.driver.get("https://rpachallengeocr.azurewebsites.net")
        time.sleep(2)

        # Criar a pasta files, caso não exista
        folder = os.getenv("FILES_FOLDER")
        os.makedirs(folder, exist_ok=True)

        # Iterar pelos invoices encontrados e baixar os desejados
        file_paths = []
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            try:
                invoice_number = int(row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
                if invoice_number in invoices:
                    url = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) a").get_attribute("href")
                    file_path = download_file(url, filename=f"{folder}/invoice_{invoice_number}")
                    file_paths.append(file_path)
                    if len(file_paths) == len(invoices):
                        break
            except Exception as e:
                print(f"Erro ao processar linha: {e}")
                continue

        # Zipar os invoices baixados sem sobrescrever os zip anteriores
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        zip_files(
            file_paths,
            zip_path=f"{folder}/invoices_{timestamp}.zip"
        )
