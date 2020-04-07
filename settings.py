DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'username' #username
PASSWORD = 'password' #password
HOST = 'mysqlip' #database ip
PORT = '3306'  #port
DATABASE = 'databasename' #database name
 
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE
    )
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
 
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5