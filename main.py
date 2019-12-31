#Main method to set up the db and also to store the information from the yaml format to the database.
import setupDB
import psycopg2
# get the connection of the database
conn = setupDB.getConnection()

# add the logic to create the tables that are needed.
curr = conn.cursor()
# check if the tables already exist otherwise create the tables.
setupDB.createTable(curr)
conn.commit()
# close the connection
setupDB.closeConnection(conn)