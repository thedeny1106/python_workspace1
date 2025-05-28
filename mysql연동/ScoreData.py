class ScoreData:
    def __init__(self, name = '', kor = 0, eng = 0, math = 0, total = 0, average = 0, grade = ''):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = total
        self.average = average
        self.grade = grade
        self.process()

    def process(self):
        self.total = self.kor + self.eng + self.math
        self.average = self.total / 3
        self.average = '수' if self.average >= 90 else '우' if self.average >= 80 else '미' if self.average >= 70 else '양' if self.average >= 60 else '가'

    def output(self):
        print(f'{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.average}\t{self.grade}')