import pymysql 

class Database:
    
    def __init__(self):
        self.db = pymysql.connect( host='localhost', user='user01', password='1234',
          db='mydb', port=3306 )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    
    #insert, update, delete
    def execute(self, query, args=()):
        print(args)
        self.cursor.execute(query, args)
        self.db.commit() 

    #데이터 딱 한개만 가져오기
    def executeOne(self, query, args=()):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone() 
        return row #결과를 반환해야 한다. 첫번째 레코드값 하나만 가져간다 

    #데이터 여러개 가져오기
    def executeAll(self, query, args=()):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall() 
        return rows #결과를 반환해야 한다. 첫번째 레코드값 하나만 가져간다 
    
    def close(self):
         if self.db.open:
            self.db.close()