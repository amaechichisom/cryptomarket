

class sql_functions:
    
    def create_database(self, database_name):
        return "CREATE DATABASE {0}".format(database_name)
    
    def drop_database(self, database_name):
        # return "DROP DATABASE {0}".format(database_name)
        return f"DROP DATABASE {database_name}"
    
    
    def select_column(self, columns, table_name):    
        return "SELECT {0} FROM {1}".format(columns, table_name)
    
    def loop_printing(self, run):
        for x in run:
            print(x)
            
    def describe_table(self, table):
        return "DESCRIBE {0}".format(table)
    
    def create_table(self, table):
        return "CREATE TABLE {0}".format(table)
    
    def select_distinct_column(self, columns, table_name):
        return "SELECT DISTINCT {0} FROM {1}".format(columns, table_name)
    
    def select_into_table(self, columns, table_name, opposite_table_name):
        return "SELECT {0} INTO {1} FROM {2}".format(columns, table_name, opposite_table_name)

    def select_top_percent(self,percent, columns, table_name):
        return "SELECT TOP {0} PERCENT {1} FROM {2}".format(percent, columns, table_name)
    
    def select_top_population(self,number, columns, table_name):
        return "SELECT TOP {0} {1} FROM {2}".format(number, columns, table_name)
    
    # def select_as(self, columns, table_name):
    #     return "SELECT {0} FROM {1}".format( columns, table_name)
    
    def select_where_column(self, columns, table_name, conditions):    
        return "SELECT {0} FROM {1} WHERE {2}".format(columns, table_name, conditions)
    
    