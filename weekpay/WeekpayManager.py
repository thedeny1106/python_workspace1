#모듈 Weekpay.py 파일에 있는 클래스 Weekpay 를 가져오겠다.
from Weekpay import Weekpay #외부파일(모듈을) 이 파일로 불러오기 

class WeekPayManager:
    
    def __init__(self):
        self.wList = [
            Weekpay("홍길동", 20, 20000),
            Weekpay("고길동", 10, 50000),
            Weekpay("김길동", 30, 40000),
            Weekpay("이길동", 40, 20000),
            Weekpay("장길동", 20, 20000)
        ]

    def output(self):
        for w in self.wList:
            w.output()


mgr = WeekPayManager()
mgr.output()

