#!/usr/bin/python
import psycopg2
from datetime import datetime
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        
        # start timestamp
        dateTimeStart = datetime.now()
        print(f'Start {dateTimeStart}')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        #conn = psycopg2.connect("dbname=plg_z3yklndp6o8l5rfv_dp user=data_admin password=aV6E!9z8q0fmTuUt port=5432")
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        #cur.execute('SELECT version()')
        cur.execute('SELECT * FROM datasource')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
    dateTimeStop = datetime.now()
    print(f'Stop {dateTimeStop}')

    delta = dateTimeStop - dateTimeStart
    print (f'Delta time {delta}')

    print(f'Delta in millisecond: {int(delta.total_seconds() * 1000)}') # Milliseconds


if __name__ == '__main__':
    connect()

