import os
import psycopg2
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
                    where (date between '{}' and '{}'); '''


@app.get("/api/dados")
def get_dados():
    pass
