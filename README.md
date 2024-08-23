**# Desafio Técnico Crawler**

#### Table of contest:

## Table of Contests:
   [objective](#objective))
   [instalation](#instalation))
   [contribution](#contribution))
   [license](#license)

## Objective

O projeto que exeutar a ação de um crawler que realizar consultas em página e extrai informações e salva os valores em arquivo e persiste os valores no banco de dados.

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
