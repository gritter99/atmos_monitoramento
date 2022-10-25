import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv(
    dotenv_path='C:/Users/Daniela Ritter/Desktop/monitoramento/atmos_monitoramento/.env')


app = Flask(__name__)

# comandos sql
dados_sql = ''' select * from monitoramento; '''

ultimo_dado_sql = '''select * 
                    from monitoramento
                    order by date desc
                    limit 1 '''

intervalo_sql = '''  select *
                    from monitoramento
                    where (date between '{}' and '{}') and mac = '{}'; '''

medias_tempo_sql = '''  select 	avg(rssi)::float as rss1_medio, avg(va) as VAm, avg(vb) as VBm, avg(vc) as VCm, 
		                        avg(ia) as IAm, avg(ib) as IBm, avg(ic) as ICm,
		                        avg(wa) as WAm, avg(wb) as WBm, avg(wc) as WCm,
		                        EXTRACT(EPOCH FROM (timestamp'{}' - timestamp'{}'))::float AS segundos
                        from monitoramento
                        where (date between '{}' and '{}') and mac = '{}'
                        group by segundos;'''
intervalo_segundos_sql = '''select 	
		                        EXTRACT(EPOCH FROM (timestamp'{}' - timestamp'{}'))::float AS segundos
                        from monitoramento
                        where (date between '{}' and '{}') and mac = '{}'
                        group by segundos;'''


@app.get("/api/dados")
def get_dados():
    try:
        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(dados_sql)
        res = [dict((cursor.description[i][0], value)
               for i, value in enumerate(row)) for row in cursor.fetchall()]

        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.get("/api/ultimo_dado")
def get_ultimo_dado():
    try:
        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(ultimo_dado_sql)
        res = [dict((cursor.description[i][0], value)
               for i, value in enumerate(row)) for row in cursor.fetchall()]

        return jsonify(res)

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
        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(intervalo_sql.format(data_inicio, data_final, mac))
        res = [dict((cursor.description[i][0], value)
               for i, value in enumerate(row)) for row in cursor.fetchall()]

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
        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(medias_tempo_sql.format(
            data_final, data_inicio, data_inicio, data_final, mac))
        res = [dict((cursor.description[i][0], value)
               for i, value in enumerate(row)) for row in cursor.fetchall()]

        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.get("/api/intervalo_segundos")
def get_intervalo_segundos():
    dados = request.get_json()
    mac = dados["mac"]
    data_inicio = dados["data_inicio"]
    data_final = dados["data_final"]
    try:
        conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(intervalo_segundos_sql.format(
            data_final, data_inicio, data_inicio, data_final, mac))
        res = [dict((cursor.description[i][0], value)
               for i, value in enumerate(row)) for row in cursor.fetchall()]

        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
