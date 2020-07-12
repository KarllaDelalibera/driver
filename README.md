[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Repositório destinado a criação de drivers 

1. **Driver de conexão: psycopg2**

  O objetivo desse driver é facilitar a conexão do usuário a qualquer banco que tenha como facilitador a biblioteca Psycopg2 do python.
  
2. **Driver de conexão: MySQL**

  O objetivo desse driver é facilitar a conexão do usuário a um banco MySQL utilizando a biblioteca mysql-connector-python do python.

# O que você consegue fazer com esses drivers

- [X] Iniciar uma conexão ao banco.
- [X] Enviar consultas para serem executas e/ou obter seus resultados.
- [X] Finalizar as conexões criadas. 

# Como utilizar

No terminal, clone o projeto:

```
git clone https://github.com/KarllaDelalibera/Driver.git
```

Entre na pasta Driver e com o Python (3 >=3.6) instalado, execute:

``` python
from driver_conexao_mysql import database as driver_sql
from driver_conexao_psycopg2 import database as driver_psy
```


> Status do Projeto: Em desenvolvimento :construction:
