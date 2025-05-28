from sqlalchemy import text
from DBEngine import theEngine
from ScoreData import ScoreData

class ScoreManager:
    def __init__(self):
        self.conn = theEngine.connect()
        self.scoreList = []
        self.setList('')

    def printList(self, sql):
        sql = 'select * from tb_score'
        result = self.conn.execute(text(sql))
        for r in result.mappings().all():
            s = ScoreData(r['sname'], r['kor'], r['eng'], r['math'])
            s.output()

    def insert(self, *args):
        sql = 'insert into tb_score(sname, kor, eng, math) values (:sname, :kor, :eng, :math)'
        self.conn.execute(text(sql), {'sname' : args[0], 'kor' : args[1], 'eng' : args[2], 'math' : args[3]})
        self.conn.commit()
        self.printList('')

    def setList(self, sql):
        sql = 'select * from tb_score'
        result = self.conn.execute(text(sql))
        for r in result.mappings().all():
            s = ScoreData(r['sname'], r['kor'], r['eng'], r['math'])
            self.scoreList.append(s)

    def gradeStatistics(self):
        sql = """select case 
        when (kor + eng + math) / 3 >= 90 then '수'
        when (kor + eng + math) / 3 >= 80 then '우'
        when (kor + eng + math) / 3 >= 70 then '미'
        when (kor + eng + math) / 3 >= 60 then '양'
        else '가' end grade
        , count(*) cnt from tb_score group by grade"""
        result = self.conn.execute(text(sql))
        print(result.mappings().all())
            
manager = ScoreManager()
manager.printList('')
manager.insert('tmp', 10, 10, 10)
manager.gradeStatistics()