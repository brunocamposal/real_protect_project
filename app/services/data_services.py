import psycopg2
import csv
from os import getenv
from http import HTTPStatus

#Função que abre e disponibiliza o arquivo utilizado por toda a aplicação
def read_csv():
    with open('auth.log', newline='') as f:
        reader = csv.reader(f)
        data_list = []
        for row in reader:
            data_list.append(row)
        return data_list

#Função que cria o caminho de conexão com o banco de dados
def create_conn_cur():

    connection_string = "host='{}' dbname='{}' user='{}' password='{}' port='{}'".format(getenv("HOST"), getenv("DBNAME"), getenv("USER"), getenv("PASSWORD"), '5432')

    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()

    return conn, cur

#Função que estabelece a conexão com o banco de dados
def query_execute(*query):
    conn, cur = create_conn_cur()

    cur.execute(*query)

    try: 
        register = cur.fetchall()
    except:
        return {"data": []}, HTTPStatus.BAD_REQUEST

    conn.commit()

    cur.close()
    conn.close()

    return register

#Função que manipula as Strings utilizadas pela função insert_data_services
def string_treatment(row):
    line = row.replace("  "," ")
    line = line.replace(" ","*",1)
    line = line.replace(" ", ",",4)
    line = line.replace("*"," ")
    line = line.split(",")
    return line

#Função que estrai as informaçãos do arquivo principal da aplicação e salva no Banco de dados
def insert_data_services():
    file_data = read_csv()

    for row in file_data:
        line = string_treatment(row[0])
        insert_table_query = """
            INSERT INTO database_auth
            (date, hours, ip, message_code, message) values
                (%s, %s, %s, %s, %s);
            """,(line[0],line[1],line[2],line[3],line[4])
        query_execute(*insert_table_query)

#Função responsavel por fazer o requerimento de todas as mensagensdo banco de dados atraves da função query_execute
def get_all_data_services():
    query = f"""SELECT * FROM database_auth"""

    execute = query_execute(query)

    return execute

#Função responsavel por fazer o requerimento das mensagensdo filtradas do banco de dados atraves da função query_execute
def get_filtered_data(data, filter):
    query = f"""SELECT * FROM database_auth as da WHERE da.{filter} LIKE '{data["data"]}%'"""

    execute = query_execute(query)

    return execute