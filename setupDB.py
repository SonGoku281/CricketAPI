import psycopg2
from configure import configure
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = configure()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
   # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
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
 
 
def getConnection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = configure()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn
def closeConnection(conn):
    if conn is not None:
        conn.close()

def createTable(cur,tableName):
    statements = ("""CREATE TABLE public.matchinfo
(
    "matchID" uuid NOT NULL,
    "venueID" uuid NOT NULL,
    gender cstring[] NOT NULL,
    "matchType" cstring[] NOT NULL,
    overs numeric NOT NULL,
    "matchResultID" uuid NOT NULL,
    PRIMARY KEY ("matchID")
)
WITH (
    OIDS = FALSE
)""",

"""ALTER TABLE public.matchinfo
    OWNER to postgres;
COMMENT ON TABLE public.matchinfo
    IS 'Contians the information of a particular match'""")
    cur.execute()


def createDBTables(conn):
    cur = conn.cursor()
    cur.execute("select exists(select * from cricket.tables where table_name=%s)", ('matchinfo',))
    exists = cur.fetchone()[0]
    # if the matchinfo table exists then do not create it and continue
    if exists == True:
        createTable(cur,"matchinfo")

    # check the same for all the other tables




# if __name__ == '__main__':
#     connect()
# else:
#     connect()