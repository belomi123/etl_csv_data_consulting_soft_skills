# Let's Import the required libraries. 
import csv
import pandas as pd
#Pandas is used to import the CSV file into Python and create a DataFrame. 
import pyodbc. 
#Pyodbc is used to connect Python to the SQL Server. 

#Let's Import the csv into a DataFrame
data = pd.read_csv (r'path/DATA.csv') 
df = pd.DataFrame(data) 
print(df)

#Let's Connect Python to the SQL Server
#Let's assume that the name of the serveur is my_server, and the name of the database is my_database. 
conn = pyodbc.connect('Driver={SQL Server}                ;' 'Server=my_server;' 
               'Database=my_database;'                   'Trusted_Connection=yes;') 
cursor = conn.cursor()

#Let's Create a Table in the SQL Server. 
cursor.execute("CREATE TABLE  DATA (id,                 first_name, last_name, email               , gender, ip_address);")

#Let's do some transformation on the data.
my_database.transform(DATA) 

#Let's Insert the DataFrame Data into the Table.
rows = [(i['id'], i['first_name'], i['last_name'], i['email'], i['gender'], i['ip_address']) for i in data]
for row in df.itertuples(): 
    cursor.execute("INSERT INTO DATA (id,           first_name, last_name, email,             gender, ip_address) VALUES (?,            ?, ?, ?, ?, ?);", rows)
conn.commit()

#Let's check if the data is safely loaded.
select * from DATA

#Let's close the  db connection
conn.close()