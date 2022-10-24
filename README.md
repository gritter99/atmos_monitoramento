# atmos_monitoramento

Repositório para o projeto de monitoramento inteligente - ATMOS

O objetivo é pegar os dados do medidor através das mensagens no broker, 
adicionar ao banco de dados (no caso utilizei apenas uma tabela com todos os valores) e
fazer uma api de busca para esses valores fornecendo o mac e o intervalo de tempo que 
queremos obter as informações.

bibliografia:

    bancos de dados:
        https://www.postgresqltutorial.com/postgresql-python/

    lidar com o broker:
        https://www.hivemq.com/blog/mqtt-client-library-paho-python/
        https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

    api:
        https://realpython.com/api-integration-in-python/
        https://blog.teclado.com/first-rest-api-flask-postgresql-python/
