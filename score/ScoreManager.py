from ScoreData import ScoreData
#ScoreData.py 파일에서 ScoreData 클래스를 가져와라 

class ScoreManager:
    def __init__(self): #생성자-파이썬에서는 변수도 만들고 
                        #첫 시작시 준비작업 
        self.scoreList = [
            ScoreData(),
            ScoreData("조승연", 90, 80, 90),
            ScoreData("안세영", 80, 80, 70),
            ScoreData("김연경", 90, 90, 90),
            ScoreData("김연아", 100, 80, 100)
        ]
    
    def printAll(self):
        for s in self.scoreList:
            s.print()

    def menuDisplay(self):
        print("--------")
        print("  메뉴   ")
        print("--------")
        print("1. 추가  ")
        print("2. 출력  ")
        print("3. 검색  ") #이름
        print("4. 수정  ") #이름
        print("5. 삭제  ") #이름
        print("6. 정렬  ") #총점 내림차순으로 
        print("0. 종료  ")
        print("--------")
        
    def append(self):
        sc =  ScoreData() #객체 생성 
        sc.name = input("이름 : ")
        sc.kor = int(input("국어 : "))
        sc.eng = int(input("영어 : "))
        sc.mat = int(input("수학 : "))
        sc.process()
        self.scoreList.append(sc)


    def start(self):
        #함수주소를 배열에 저장하고 호출함 ,
        funcList =[None, self.append, self.printAll]    
        while True:
            self.menuDisplay()
            choice = int(input("선택 : "))
            if choice>0 and choice<len(funcList):
                funcList[choice]()
            elif choice==0:
                return 
            else:
                print("잘못된 메뉴입니다.")


if __name__ =="__main__":
    sm = ScoreManager()
    sm.start()

