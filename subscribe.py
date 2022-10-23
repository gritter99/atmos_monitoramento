import paho.mqtt.client as paho
import ast
import psycopg2


# fazer a inscricao na atmos-message para obter os dados
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


# durante a analise da mensagem ja aproveito para adicionar os dados no banco de dados
def on_message(client, userdata, msg):
    # transformar string em um dicionario
    dados = ast.literal_eval(msg.payload.decode("utf-8"))

    add_dados_no_banco('''
            INSERT INTO monitoramento(mac, date, rssi, va, vb, vc, ia, ib, ic, wa, wb, wc) 
            VALUES('{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {});
            
            '''.format(dados['mac'], dados['date'], dados['rssi'], dados['va'], dados['vb'], dados['vc'], dados['ia'], dados['ib'], dados['ic'], dados['wa'], dados['wb'], dados['wc']))


# funcao para fazer a adicao dos valores que vai ser utilizada durante a recepcao da mensagem
def add_dados_no_banco(query):
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
        print('adicionando valor na tabela...')
        cur.execute(query)
        cur.close()

        # commit the changes
        conn.commit()

    # tratar as excecoes
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # finalizar a conexao
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':

    client = paho.Client()
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.connect('broker.hivemq.com', 1883)
    client.subscribe('/atmos-message')

    client.loop_forever()

# fontes utilizadas:
# https://www.hivemq.com/blog/mqtt-client-library-paho-python/
# https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
