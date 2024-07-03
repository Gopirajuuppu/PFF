import sqlite3


class SQLiteDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name, columns):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            columns_str = ', '.join([f'{col_name} {col_type}' for col_name, col_type in columns.items()])
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
            self.conn.commit()
        except Exception as error:
            print("`create_table` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def drop_table(self, table_name):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
            self.conn.commit()
        except Exception as error:
            print("`drop_table` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def insert_multiple_rows(self, table_name, rows):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.executemany(f'INSERT INTO {table_name} VALUES ({",".join(["?" for _ in rows[0]])})', rows)
            self.conn.commit()
        except Exception as error:
            print("`insert_multiple_rows` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def insert_single_row(self, table_name, row):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'INSERT INTO {table_name} VALUES ({",".join(["?" for _ in row])})', row)
            self.conn.commit()
        except Exception as error:
            print("`insert_single_row` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def delete_multiple_rows(self, table_name, condition):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'DELETE FROM {table_name} WHERE {condition}')
            self.conn.commit()
        except Exception as error:
            print("`delete_multiple_rows` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def delete_single_row(self, table_name, condition):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'DELETE FROM {table_name} WHERE {condition} LIMIT 1')
            self.conn.commit()
        except Exception as error:
            print("`delete_single_row` Error: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            self.close()

    def fetch_data(self, table_name, columns='*', condition=None):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            if condition:
                cursor.execute(f'SELECT {columns} FROM {table_name} WHERE {condition}')
            else:
                cursor.execute(f'SELECT {columns} FROM {table_name}')
            data = cursor.fetchall()
        except Exception as error:
            print("`fetch_data` Error: {}".format(error))
            data = "ERROR"
        finally:
            if cursor:
                cursor.close()
            self.close()
        return data
    
    def fetch_query(self, query):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        except Exception as error:
            print("`fetch_query` Error: {}".format(error))
            data = "ERROR"
        finally:
            if cursor:
                cursor.close()
            self.close()
        return data
    
    # to update the database table with query 
    def update_query(self,query):
        self.connect()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query) 
            self.conn.commit()
        except Exception as error:
            print("`update_query` Error: {}".format(error))
            data = "ERROR"
        finally:
            if cursor:                
                cursor.close()
            self.close()
        #print(" Updated the table with the query--:",query)


def delete_incomplete_chat():
    #delete_query = """ DELETE FROM conversation_log_table WHERE Chat_Type='chat_incomplete' """
    delete_query = """ DELETE FROM conversation_log_table WHERE conversation_id='19042024072959' """
    form_fill_db.update_query(delete_query)
    print('-- Deleted all previsous chats ---')

form_fill_db = SQLiteDatabase('./DB/form_fill.db')

# form_fill_db.drop_table('conversation_log_table')
# print('-- Deleted the table conversation_log_table ---')

# #creating conversation_log_table table
# form_fill_db.create_table("conversation_log_table",
#                      {
#                          "conversation_id": "VARCHAR",
#                          "name": "VARCHAR",
#                          "date_time": "VARCHAR",
#                          "role": "VARCHAR",
#                          "text": "BLOB",
#                          "section": "VARCHAR",
#                          "Chat_Type":"VARCHAR",
#                          "Mcq_Type":"VARCHAR" ,
#                          "audio": "BLOB"   
#                      })
# print('-- created the table conversation_log_table ---')

# #creating speech_conversation_table
# form_fill_db.create_table("speech_conversation_table",
#                      {
#                          "conversation_id": "VARCHAR",
#                          "name": "VARCHAR",
#                          "date_time": "VARCHAR",
#                          "role": "VARCHAR",
#                          "text": "BLOB",
#                          "section": "VARCHAR",
#                          "Chat_Type":"VARCHAR",
#                          "Mcq_Type":"VARCHAR",
#                          "audio": "BLOB"  
#                      })
# print('-- created the table speech_conversation_table ---')

# Fecth Query
# fetch_query = """ select Mcq_Type from conversation_log_table WHERE conversation_id='02052024163939' """ 
# data = form_fill_db.fetch_query(fetch_query)
# #print(data)
# print(data[1][0])

#conversation_log_table
#analyzed_conversation
#22052024154830

#Fecth Query
#fetch_query = """ select * from analyzed_conversation WHERE conversation_id='22052024154830' """ 
#data = form_fill_db.fetch_query(fetch_query)
#print(data[0][4])

#Fecth Query
#fetch_query = """ select DISTINCT conversation_id from analyzed_conversation """ 
#fetch_query = """ select DISTINCT conversation_id from conversation_log_table """
fetch_query = """ select conversation_id,role,text,Chat_Type from conversation_log_table where conversation_id='27062024173406' """
#fetch_query = "PRAGMA table_info(conversation_log_table) "
#fetch_query = """ SELECT conversation_id,role,text FROM speech_conversation_table where conversation_id='27062024164956' """
data = form_fill_db.fetch_query(fetch_query) 
print(data)
#print(data[0])
#con_list = ['11042024053947','11042024061638','23042024124223','03052024122643','03052024130023','06052024114906','06052024131440','08052024165329','08052024173047','08052024174444']

# Deelete Query
#delete_query = """ DELETE FROM analyzed_conversation WHERE conversation_id='22052024154830' """
#delete_query = """ DELETE FROM analyzed_conversation WHERE conversation_id in ('22052024154830','13062024141341') """
#delete_query = """ DELETE FROM conversation_log_table WHERE conversation_id in ('22052024154830','13062024102757','13062024140700','13062024140723','13062024141341','19062024134351','24062024123208','25062024125500') """
#form_fill_db.update_query(delete_query)
#print('-----deleted -----')



