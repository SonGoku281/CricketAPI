#Main method to set up the db and also to store the information from the yaml format to the database.
import psycopg2
import getCrickSheetData
import parseAllMatchesYaml
import setupDB
#get all the data from cricksheet
#getCrickSheetData.getDatafromCrickSheet()
# get the connection of the database
conn = setupDB.getConnection()
# add the logic to create the tables that are needed.
curr = conn.cursor()
# check if the tables already exist otherwise create the tables.
curr.execute("select exists(select * from information_schema.tables where table_name=%s)", ('matchmetainfo',))
exists = curr.fetchone()[0]
if  exists == False:
    setupDB.createTable(curr)
    conn.commit()
# update the tables
parseAllMatchesYaml.parseMatches(curr)
conn.commit()
# close the connection
setupDB.closeConnection(conn)