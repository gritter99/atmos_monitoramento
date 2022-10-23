import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path='C:/Users/Daniela Ritter/Desktop/monitoramento/atmos_monitoramento/.env')


# funcao apenas para conectar com o banco de dados e criar a tabela
def create_table_monitoramento():
    try:
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'))

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('criando tabela monitoramento')

        cur.execute('''
            create table if not exists monitoramento(
            
            mac macaddr not null, 
            date timestamp  not null,
            rssi integer NOT NULL,
            va numeric not null,
            vb numeric not null,
            vc numeric not null,
            ia numeric not null,
            ib numeric not null,
            ic numeric not null,
            wa numeric not null,
            wb numeric not null,
            wc numeric not null
            
            )
            
            '''
                    )

        cur.close()

        # commit the changes
        conn.commit()

    # printar os erros
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('conexao finalizada.')


if __name__ == '__main__':
    create_table_monitoramento()
