from me.reb4ck.prode.repository.UserRepository import UserRepository
import pymysql


class MySQLUserRepository(UserRepository):
    def __init__(self, config):
        self.connection = pymysql.connect(host=config.host,
                             user=config.user_name,
                             password=config.password,
                             database=config.db_type,
                             cursorclass=pymysql.cursors.DictCursor)

        self.create_table()

    def create_table(self):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE TABLE Persons (PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255), City varchar(255));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()

    def add_table(self):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()


