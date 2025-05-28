#pip install sqlalchemy 
#버전 2.0이상 
#C:\Users\littl\AppData\Roaming\Python\Python38\site-packages\sqlalchemy
#https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/1.%20%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC%20%EA%B0%9C%EC%9A%94.html#%E1%84%8C%E1%85%A6%E1%84%80%E1%85%A9%E1%86%BC%E1%84%83%E1%85%AC%E1%84%82%E1%85%B3%E1%86%AB-%E1%84%80%E1%85%A5%E1%86%BA

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:1234@localhost/mydb",
    pool_size=10,         # 최대 연결 수
    max_overflow=5,       # 초과 시 추가 연결 수
    pool_recycle=3600     # 재활용 시간
)

# 1.데이터 가져오기
with engine.connect() as conn:
    sql = '''
        select empno, ename, sal
        from emp
    '''
    result = conn.execute(text(sql))
    for row in result.all(): print(row)

    result = conn.execute(text(sql))
    rows = result.mappings().all()
    for row in rows: print(dict(row))

# 2. 검색어를 전달할 때
ename = '조승연'

with engine.connect() as conn:
    sql = '''
        select empno, ename, sal
        from emp
        where ename = :name
    '''
    result = conn.execute(text(sql), [{'name':ename}])
    result = result.all()
    if not result: print('없음')
    else: print(r for r in result)

# 3. insert
with engine.connect() as conn:
    sql = '''select max(empno) + 1 from emp'''
    empno = conn.execute(text(sql)).all()[0][0]
    sql = '''
        insert into emp(empno, ename, sal)
        values(:empno, :ename, :sal)
    '''
    conn.execute(text(sql), [{'empno' : empno, 'ename' : f'tmp{empno}', 'sal' : 9000}])
    conn.commit()
    
# 3. insert
with engine.connect() as conn:
    sql = '''select ifnull(max(id), 0) + 1 from test1'''
    id = conn.execute(text(sql)).all()[0][0]
    sql = '''
        insert into test1(id, field)
        values(:id, :field)
    '''
    conn.execute(text(sql), [{'id' : id, 'field' : 'test'}])
    
    sql = '''select ifnull(max(id), 0) + 1 from test2'''
    id = conn.execute(text(sql)).all()[0][0]
    sql = '''
        insert into test2(id, field)
        values(:id, :field)
    '''
    conn.execute(text(sql), [{'id' : id, 'field' : '0192384035604365035'}])
    conn.commit()