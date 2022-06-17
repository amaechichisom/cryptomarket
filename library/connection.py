import mysql.connector

def create_db_connection(host_name, user_name, user_password,port_number, db_name=None):
    connection = None
    try:
        if(db_name == None):
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                port=port_number,
                auth_plugin='mysql_native_password')
            print("MySQL database connection successfull")
        else:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                port=port_number,
                auth_plugin='mysql_native_password',
                database=db_name)
            print("MySQL database connection successfull")
    
    except Exception as err:
        print(f"Error: '{err}'")
        
    return connection