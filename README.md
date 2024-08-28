# # Desafio Técnico Crawler

## Table of Contests:
  - [Objective](#objective)
  - [Instalation](#instalation)
  - [Contribution](#contribution)
  - [License](#license)

## Objective

O objetivo deste projeto é realizar a requisição da url e fazer a extração dos valores por meio da biblioteca BeautifoulSoup e salvar os valores obtidos em um arquivo json, que posteriormente será no banco de dados.

Para o desenvolvimento do projeto foi utilizado a linguagem python.

### Bibliotecas utilizadas:

- BeautifulSoup
- Requests

Para realizar as consultas é necessário alterar o arquivo json

## Instalation 

   Clone the repository 

   git clone https://github.com/vanessaformiga/desafio_tecnico_crawler.git


   Instalação necessária para um ambiente virtual
   - pip install virtualenv

   Criando uma nova virtualenv 
   - python -m venv venv 

   Ativando um nova ambiente virtualvenv
   - venv/Scripts/Activate (windows)
   - venv/bin/activate (linux )

   Desativando um ambiente virtualvenv
   - venv deactivate

   Gerar o arquivo 
   - pip freeze > requirements.txt

   Instalando dependências
   - pip install -r requirements.txt

   Para alterar o arquivo json para realizar as consultas
   arquivo_de_consulta.json

## Contribution

### Decisões de implementação

Uma das decisões tomadas foi criar um arquivo json, que possui os códigos dos valalores que podem ser utilizados para fazer as consultas. 

### Sobre as dificuldades Encontradas

## License

Este projeto foi criado por Vanessa Formiga
