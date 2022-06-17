
from connection.connection import create_db_connection
from connection.sql_functions import sql_functions

db =create_db_connection(host_name="localhost", user_name="root", user_password="legend@1997", port_number='3306', db_name='testdatabase')

running = db.cursor()
cursor = sql_functions()

running.execute(cursor.create_database('pearly'))

running.execute(cursor.select_column("first_name, created", 'Test'))

# cursor.loop_printing(running)

# running.execute(cursor.create_table("boss(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"))

# running.execute(cursor.describe_table("boss"))

# cursor.loop_printing(running)