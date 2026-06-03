import mysql.connector

def get_database_connection():
     connection = mysql.connector.connect(
         host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
         user = '2nQJAqXtCY6ykeT.root',
         password = 'j89fKniynldfqnyV',
         database = 'student_task_manager',
         port = 4000
     )

     return connection