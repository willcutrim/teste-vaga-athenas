# Executando o Django com Docker

Este repositório contém um ambiente Docker pré-configurado para executar um aplicativo Django com um banco de dados PostgreSQL.

## Pré-requisitos

Antes de começar, certifique-se de ter o Docker e o Docker Compose instalados no seu sistema. Você pode encontrar instruções de instalação em [docker.com](https://www.docker.com/get-started) e [docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

## Executando o Docker Compose

1. Clone este repositório para o seu sistema local:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git


2. Entre na pasta:

   ```bash
   cd seu-repositorio  


3. Execute o docker:

   ```bash
   docker-compose up 

4. Execute as migrações em outro terminal:

   ```bash
   python manage.py makemigrations && python manage.py migrate


5. instale os pacotes:

   ```bash
   pip install -r requirements.txt
   
6. Rode o projeto e seja feliz:

   ```bash
   python manage.py runserver


Este README fornece instruções passo a passo para executar o Docker, executar as migrações do Django e iniciar o servidor Django. Certifique-se de personalizar as instruções de acordo com a estrutura e as necessidades específicas do seu projeto.
