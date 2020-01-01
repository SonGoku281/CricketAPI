import psycopg2
from configure import configure
import uuid
class Venue:
  def __init__(self,stadium):
    self.stadium = stadium

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

    

def createTable(cur):
    sqlCreateMatchMetaTable = "create table matchMetainfo ( matchMetaID varchar NOT NULL, matchID uuid NOT NULL, creationDate date NOT NULL, dataVersion numeric NOT NULL, revision numeric NOT NULL, PRIMARY KEY (matchMetaID) )"
    sqlCreateMatchInfoTable = "create table matchInfo ( matchID uuid NOT NULL, venueID uuid NOT NULL, gender varchar NOT NULL, matchType varchar NOT NULL, overs numeric NOT NULL, matchResultID uuid NOT NULL,PRIMARY KEY (matchID))"
    sqlCreateMatchResultTable = "create table matchResult ( matchResultID uuid NOT NULL, matchID uuid NOT NULL, firstTeam uuid NOT NULL, secondTeam uuid NOT null, result varchar NOT NULL, winningTeam uuid , playerOfMAtch uuid, toss uuid, PRIMARY KEY (matchResultID))"
    sqlCreateVenueTable = "create table venue ( venueID uuid NOT NULL, stadium text NOT NULL, PRIMARY KEY (venueID))"
    cur.execute(sqlCreateMatchMetaTable)
    cur.execute(sqlCreateMatchInfoTable)
    cur.execute(sqlCreateMatchResultTable)
    cur.execute(sqlCreateVenueTable)
    return

def createDBTables(conn):
    cur = conn.cursor()
    cur.execute("select exists(select * from cricket.tables where table_name=%s)", ('matchinfo',))
    exists = cur.fetchone()[0]
    # if the matchinfo table exists then do not create it and continue
    if exists == True:
        createTable(cur,"matchinfo")

    # check the same for all the other tables

def updateTables(cur,datamap,filename):
    # implement the logic to read each file in the ./allMatches folder and get update the data in the tables.
    # insert data into the venue table
    VenueObject = Venue(datamap['info']['venue'])
    venueID = updateVenue(cur,VenueObject)
    return

def updateVenue(cur,VenueObject):
    sql = "INSERT INTO venue(venueid,stadium) VALUES(%s,%s)"
    venueID = uuid.uuid4().hex
    cur.execute(sql,(venueID,VenueObject.stadium,))
    return venueID

def updateMatchMetaTable(cur,matchObject):
    # update the meta match table
    sql = " INSERT INTO matchinfo(matchid,venueid,gender,matchtype,overs,matchresultid) VALUES(%s,%s,%s) "
    return
# if __name__ == '__main__':
#     connect()
# else:
#     connect()