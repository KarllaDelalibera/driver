[![python](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)

# Repositório destinado a criação de drivers de conexão com banco de dados

1. **Driver de conexão: psycopg2**

  O objetivo desse driver é facilitar a conexão do usuário a qualquer banco que tenha como facilitador a biblioteca Psycopg2 do python.
  
2. **Driver de conexão: MySQL**

  O objetivo desse driver é facilitar a conexão do usuário a um banco MySQL utilizando a biblioteca mysql-connector-python.

# O que você consegue fazer com esses drivers

- [X] Iniciar uma conexão ao banco.
- [X] Enviar consultas para serem executas e/ou obter seus resultados.
- [X] Finalizar as conexões criadas. 

# Como utilizar

No terminal, clone o projeto:

```
git clone https://github.com/KarllaDelalibera/driver.git
```

Entre na pasta driver e com o Python instalado, execute:

``` python
from driver_conexao_mysql import database as driver_sql
from driver_conexao_psycopg2 import database as driver_psy
```


> Status do Projeto: Em desenvolvimento :construction:
