from DBModule import Database 

class ScoreData:
    def __init__(self, sname="", kor=0, eng=0, mat=0,  
                 total=0, average=0):
        self.sname = sname 
        self.kor = kor 
        self.eng = eng
        self.mat = mat 
        self.total = total 
        self.average=average  
    
    def output(self):
        print(self.sname, self.kor, self.eng, self.mat , 
              self.total, self.average )
        
class ScoreManager :
    def append(self):
        s = ScoreData()
        s.sname = input("이름 : ")
        s.kor = input("국어 ")
        s.eng = input("영어 ")
        s.mat = input("수학 ")
        sql = '''
            insert into tb_score(sname, kor, eng, mat, regdate)
            values( %s, %s,%s,%s, now())
        '''
        db = Database()
        db.execute(sql, (s.sname, s.kor, s.eng, s.mat))
        db.close() 

    def output(self):
        sql = """
            select sname, kor, eng, mat 
            ,(kor+eng+mat) as total 
            ,(kor+eng+mat)/3 as average 
            from tb_score 
        """
        db=Database()
        rows = db.executeAll(sql)
        self.dataList = [] 
        for r in rows:
            s = ScoreData(r['sname'], r['kor'], r['eng'],
                          r['mat'], r['total'], r['average'])
            self.dataList.append(s)

        for s in self.dataList:
            s.output()

if __name__ =="__main__":
    sm = ScoreManager()
    sm.output()

