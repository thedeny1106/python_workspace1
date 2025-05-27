#pip install sqlalchemy pymysql

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:1234@localhost/mydb",
    pool_size=10,         # 최대 연결 수
    max_overflow=5,       # 초과 시 추가 연결 수
    pool_recycle=3600     # 재활용 시간
)

try:
    conn = engine.connect()
    result = conn.execute("SELECT DATABASE();")
    print("연결 성공, 현재 DB:", result.scalar())
except Exception as e:
    print("연결 실패:", e)
finally:
    conn.close()

try:
    conn = engine.connect()
    print("데이터베이스 연결 성공")
except SQLAlchemyError as e:
    print("데이터베이스 연결 실패:", e)



result = conn.execute(text("SELECT * FROM emp"))

# for row in result:
#     print(row)
rows = result.mappings().all()
for row in rows:
        print(dict(row))


conn.close()