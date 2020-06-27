import json
import logging
import psycopg2
import psycopg2.extras

logger = logging.getLogger('POSTGRESQL')
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
            self.conn = psycopg2.connect(host=self.host,
                                         user=self.username,
                                         password=self.password,
                                         port=self.port,
                                         dbname=self.dbname)
            return self.conn
        except psycopg2.DatabaseError as e:
            logger.error(e)

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def execute_query_return_json(self, query):
        '''
        Executa uma consuta no banco e retorna o resultado em formato json
        '''
        try:
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.cur.execute(query)
            return json.dumps(self.cur.fetchall())
        except psycopg2.Error as e:
            logger.error(e.pgerror) 
        finally:
            self.cur.close()

    def execute_query(self, query, parameter=None):
        try:
            self.cur = self.conn.cursor()
            if parameter is None:
                self.cur.execute(query)
                self.conn.commit()
            else:
                self.cur.execute(self.cur.mogrify(query, parameter))
                self.conn.commit()
        except psycopg2.Error as e:
            logger.error(e.pgerror)
        finally:
            self.cur.close()
