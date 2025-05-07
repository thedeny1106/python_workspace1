class Weekpay:
    def __init__(self, name="", work_time=20, per_pay=10000):
        self.name = name 
        self.work_time=work_time
        self.per_pay=per_pay
        self.process() #클래스 내부 함수 호출시 self로 해야 한다 

    def process(self):
        self.pay = self.work_time * self.per_pay

    def output(self):
        print(f"{self.name} {self.work_time} {self.per_pay} {self.pay}")


w1 = Weekpay("A")
w1.output()