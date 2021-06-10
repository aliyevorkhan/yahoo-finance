import sqlite3
from sqlite3 import Error

create_table_query = ''' CREATE TABLE IF NOT EXISTS %s (
                                    date text,
                                    open real,
                                    high real,
                                    low real,
                                    close real,
                                    adj_close real,
                                    volume integer
                                ); '''


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_query statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, row, company):
    """ insert a data to the table with insert_data_query statement
    :param conn: Connection object
    :param row: values for given row of table
    :param company: table_name
    :return:
    """
    insert_data_query = ''' INSERT INTO {} (date,open,high,low,close,adj_close, volume)
                VALUES(?,?,?,?,?,?,?) '''.format(company)
    try:
        cur = conn.cursor()
        cur.execute(insert_data_query, row)
        conn.commit()
    except Error as e:
        print(e)

def get_data_from_table(conn, company):
    company_result_dict = {}
    select_data_query = '''SELECT * FROM {}'''.format(company)
    cur = conn.cursor()
    cur.execute(select_data_query)
    rows = cur.fetchall()
    for id, row in enumerate(rows):
        info_dict={}

        info_dict["Date"] = row[0]
        info_dict["Open"] = row[1]
        info_dict["High"] = row[2]
        info_dict["Low"] = row[3]
        info_dict["Close"] = row[4]
        info_dict["Adj_Close"] = row[5]
        info_dict["Volume"] = row[6]

        company_result_dict[str(id)] = info_dict
    return company_result_dict