# atmos_monitoramento

Repositório para o projeto de monitoramento inteligente - ATMOS

O objetivo é obter os dados do medidor por meio das mensagens no broker, adicionar ao banco de dados PostgreSQL e desenvolver uma api de busca para esses valores.

Existem rotas criadas para:
- obter todos os dados do medidor
- obter o último dado adicionado
- obter os dados do medidor em um intervalo de tempo
- obter as médias (potência, corrente e tensão) em um determinado período
- obter o tempo em segundos entre as datas definidas (para facilitar um possível cálculo com esse dado)

As 3 últimas rotas necessitam de um arquivo JSON com os parâmetros desejados.

bibliografia:

    bancos de dados:
        https://www.postgresqltutorial.com/postgresql-python/

    lidar com o broker:
        https://www.hivemq.com/blog/mqtt-client-library-paho-python/
        https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

    api:
        https://realpython.com/api-integration-in-python/
        https://blog.teclado.com/first-rest-api-flask-postgresql-python/
