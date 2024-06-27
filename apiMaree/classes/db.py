import mysql.connector
from mysql.connector import errorcode

class Db:
    """
    Gestionnaire de base de données MySQL
    """
    DEFAULT_CONFIG = {
        'user': 'anthony',
        'password': 'oketooketo',
        'host': '127.0.0.1',
        'database': 'bdd_maree'
        
    }
    connection = None
    database_config = None

    # Ouverture / fermeture de la base de données
    @classmethod
    def open(cls, database_config=DEFAULT_CONFIG):
        if cls.is_opened():
            raise RuntimeError("open: database is already opened")
        cls.database_config = database_config
        try:
            cls.connection = mysql.connector.connect(**database_config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    @classmethod
    def close(cls):
        if not cls.is_opened():
            raise RuntimeError("close: database is not opened")
        cls.connection.close()
        cls.connection = None

    @classmethod
    def is_opened(cls):
        return (cls.connection is not None)

    @classmethod
    def remove(cls, database_config):
        # Suppression de la base de données
        if cls.is_opened():
            raise RuntimeError("remove: database is currently opened")
        temp_connection = mysql.connector.connect(
            user=database_config['user'], 
            password=database_config['password'], 
            host=database_config['host']
        )
        cursor = temp_connection.cursor()
        cursor.execute(f"DROP DATABASE {database_config['database']}")
        temp_connection.close()

    # retourner un cursor
    @classmethod
    def get_cursor(cls):
        if not cls.is_opened():
            raise RuntimeError("get_cursor: database is not opened")
        return cls.connection.cursor()

    # Execution de requetes
    @classmethod
    def query_insert(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_commit: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        cls.connection.commit()
        return cursor.lastrowid

    @classmethod
    def query_commit(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_commit: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        cls.connection.commit()

    @classmethod
    def query_all(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_all: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    @classmethod
    def query_one(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_one: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)        
        result = cursor.fetchone()
        return result
