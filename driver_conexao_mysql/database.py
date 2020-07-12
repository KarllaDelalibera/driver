import logging
import mysql.connector as mysql

logger = logging.getLogger('MySQL')
logger.setLevel(logging.INFO)


class Database:

    def __init__(self, host, username, password, port, dbname):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.dbname = dbname

    def connect(self):
        try:
            self.conn = mysql.connect(host=self.host,
                                      user=self.username,
                                      passwd=self.password,
                                      port=self.port,
                                      database=self.dbname,
                                      autocommit=True)
            return self.conn
        except mysql.Error as e:
            logger.error(e)

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def execute_query_return(self, query):
        '''
        Executa uma consuta no banco e retorna o resultado
        '''
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            return self.cur.fetchall()
        except mysql.Error as e:
            logger.error(e) 
        finally:
            self.cur.close()

    def execute_query(self, query, parameter=None):
        try:
            self.cur = self.conn.cursor()
            if parameter is None:
                self.cur.execute(query)
            else:
                self.cur.execute(query, parameter)
        except mysql.Error as e:
            logger.error(e.pgerror)
        finally:
            self.cur.close()

