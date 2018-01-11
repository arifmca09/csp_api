
import MySQLdb


class MySQLOps(object):
    """
    MySQL DB CRUD Operations module
    """
    def __init__(self, hostname, username, password, database):
        """

        :param hostname: Provide MySQL hostname
        :param username: Provide MySQL username
        :param password: Provide MySQL password
        :param database: Provide MySQL database
        """
        self.db = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self._connect()

    def __del__(self):
        """
        MySQL destructor to close existing connection

        :return: None
        """
        self.db.close()

    def _connect(self):
        """
        MySQL DB connection establishment

        :return: return MySQL cursor to execute queries
        """
        self.db = MySQLdb.connect(self.hostname, self.username, self.password, self.database)

    def insert(self, table, **kwargs):
        """
        Insert row to MySQL data table

        :param table: Provide table name to insert data
        :param kwargs: Provide column name & row in parameter argument type
        :return: None
        """
        keys = kwargs.keys()
        values = tuple(kwargs.values())
        query = "INSERT INTO %s " % table + "(" + ",".join(["`%s`"] * len(keys))\
                % tuple(keys) + ") VALUES (" + ",".join(["%s"] * len(values)) + ")"
        try:
            self.db.cursor().execute(query, values)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
