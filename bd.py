# https://www.postgresqltutorial.com/postgresql-python/

import psycopg2


def create_table_monitoramento():
    """ Connect to the PostgreSQL database server """
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(
            host="localhost",
            database="monitoramento",
            user="postgres",
            password="----")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('creating table monitoramento')

        cur.execute('''
            create table monitoramento(
            
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

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    create_table_monitoramento()
