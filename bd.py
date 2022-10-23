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
            
            mac macaddr primary key, 
            date date not null,
            rssi integer NOT NULL,
            va integer not null,
            vb integer not null,
            vc integer not null,
            ia integer not null,
            ib integer not null,
            ic integer not null,
            wa integer not null,
            wb integer not null,
            wc integer not null
            
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
