from dis import findlinestarts
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv(
    dotenv_path='C:/Users/Daniela Ritter/Desktop/monitoramento/atmos_monitoramento/.env')

conn = psycopg2.connect(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user'),
    password=os.getenv('password')
)

app = Flask(__name__)

dados_sql = ''' select * from monitoramento; '''
intervalo_sql = '''  select *
                    from monitoramento
                    where (date between '{}' and '{}') and mac = '{}'; '''

medias_tempo_sql = '''  select 	avg(rssi) as rss1_medio, avg(va) as VAm, avg(vb) as VBm, avg(vc) as VCm, 
		                        avg(ia) as IAm, avg(ib) as IBm, avg(ic) as ICm,
		                        avg(wa) as WAm, avg(wb) as WBm, avg(wc) as WCm,
		                         
		                        EXTRACT(EPOCH FROM (timestamp'{}' - timestamp'{}')) AS segundos
                        from monitoramento
                        where (date between '{}' and '{}') and mac = '{}'
                        group by segundos;'''


@app.get("/api/dados")
def get_dados():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(dados_sql)
        row = cursor.fetchall()
        res = jsonify(row)
        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.get("/api/intervalo")
def get_intervalo():
    dados = request.get_json()
    mac = dados["mac"]
    data_inicio = dados["data_inicio"]
    data_final = dados["data_final"]
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(intervalo_sql.format(data_inicio, data_final, mac))
        row = cursor.fetchall()
        res = jsonify(row)
        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.get("/api/medias_tempo")
def get_media_tempo():
    dados = request.get_json()
    mac = dados["mac"]
    data_inicio = dados["data_inicio"]
    data_final = dados["data_final"]
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(medias_tempo_sql.format(
            data_final, data_inicio, data_inicio, data_final, mac))
        row = cursor.fetchall()
        res = jsonify(row)
        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
