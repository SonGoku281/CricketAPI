#Main method to set up the db and also to store the information from the yaml format to the database.
import setupDB

# get the connection of the database
conn = setupDB.getConnection()

# add the logic to create the tables that are needed.

# close the connection
setupDB.closeConnection(conn)