import psycopg2
from config import config

def connect(db_cred):
    conn = None
    try:
        params = config(db_cred)
        print("connecting to postgresql database...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print(cur, "Its Connected...")
        
        return cur

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)




    


