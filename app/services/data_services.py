import psycopg2
import csv


def read_csv():
        with open('auth.log', newline='') as f:
            reader = csv.reader(f, quotechar='|')
            data_list = []
            for row in reader:
                data_list.append(row)
            return data_list

def create_conn_cur():

    connection_string = "host='{}' dbname='{}' user='{}' password='{}' port='{}'".format('localhost', 'bd_real_protect', 'joao', '130901', '5432')

    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()

    return conn, cur

def query_execute(*query):
    conn, cur = create_conn_cur()

    cur.execute(*query)

    try: 
        register = cur.fetchall()
    except:
        register = "Query executed."

    conn.commit()

    cur.close()
    conn.close()

    return register

def insert_data_services():
    file_data = read_csv()

    for row in file_data:
        line = row[0].replace("  "," ")
        line = line.replace(" ","*",1)
        line = line.replace(" ", ",",4)
        line = line.replace("*"," ")
        line = line.split(",")
        insert_table_query = """
            INSERT INTO database_auth
            (date, hours, ip, message_code, message) values
                (%s, %s, %s, %s, %s);
            """,(line[0],line[1],line[2],line[3],line[4])
        query_execute(*insert_table_query)

def get_all_Data_services():

    get_all_Data = """SELECT * FROM database_auth;"""

    fieldnames = ["date", "hours", "ip", "message_code", "message"]

    data = []

    query = query_execute(get_all_Data)

    for Digital_data in query:
        data.append({"date":Digital_data[0],"hours":Digital_data[1],"ip":Digital_data[2], "message_code":Digital_data[3], "message":Digital_data[4]})

    return {"list_log": data}

insert_data_services()