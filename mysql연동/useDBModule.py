from DBModule import Database 

db = Database() #객체만들면 이미 디비 접근 
sql = "select * from tb_member"
rows = db.executeAll(sql)
for row in rows:
    print(row)
db.close()
