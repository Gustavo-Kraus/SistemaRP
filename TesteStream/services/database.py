import pyodbc 

server = 'WIN-5AS614VFKJO\SQLEXPRESS' 
database = 'sistemarp' 
username = 'sa' 
password = '13209' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password, Trusted_connection='yes')
cursor = cnxn.cursor()