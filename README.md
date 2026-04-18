# rpa-challenge-wellbe
Repositório para demonstrar meu conhecimento de RPA desenvolvido em Python.

Esta automação acessa um site de filmes, extrai informações sobre estes filmes, as salva em banco e então cria um csv com as informações extraídas. Depois, acessa outro site, baixa dois arquivos, e por fim os comprime em arquivo zip.


## Features v1.0
1. Acessa o site https://rpachallenge.com
2. Navega para a aba Movie Search
3. Busca pelos filmes com a string query
4. Salva no BD o nome e a descrição dos filmes encontrados, sem criar índices duplicados
5. Cria um arquivo csv e o popula com um dump do BD
6. Acessa o site https://rpachallengeocr.azurewebsites.net
7. Busca os invoices descritos na tupla e realiza o download deles
8. Cria um arquivo zip com os invoices baixados e por fim os apaga


## Parâmetros
A aplicação recebe dois parâmetros:

query - string com o nome do filme que o usuário quer buscar
invoices - tupla com os índices dos invoices que o usuário deseja baixar


## Utilização do app
1. Criar ambiente, instalar as dependências e arquivo .env:
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> cp .env.example .env
2. Alterar os parâmetros no final do arquivo main.py (opcional):
> filme = "Avengers"
> invoices = (2, 4)
3. Executar a aplicação:
> python3 src/main.py
4. Aguarde a execução. Os resultados estarão na pasta "files":
> Exemplo:
> db_dump_20260418113412320212.csv
> invoices_20260418113438040437.zip


## Funções SQL
1. Criar DB
> CREATE DATABASE rpa_db;
2. Criar usuário específico
> CREATE USER 'rpa_user'@'localhost' IDENTIFIED BY 'strong_password';
3. Dá permissões ao usuário
> GRANT ALL PRIVILEGES ON rpa_db.* TO 'rpa_user'@'localhost';
> FLUSH PRIVILEGES;
4. Criar tabela
> USE rpa_db;
> CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255),
    description VARCHAR(500) UNIQUE
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Obs: description como chave única evita duplicidades de maneira mais eficiente do que apenas o nome