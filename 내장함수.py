print( abs(-4) )
print( abs(4) )
print( all( [1,2,3] )) #지금 전달받은 요소중에 0이 하나라도 존재하면 False
print( all( [1,2,3,0] )) #요소전체가 True이면 True 
                         #0, False, "" - False 
print( all( ["a", "b", "C"] ))
print( all( ["a", "b", ""] ))
 
print( any( [1,2,3] )) #지금 전달받은 요소중에 0이 아닌것이 하나라도 
#존재하면 True
print( any( [1,2,3,0] ))

###################################
print( dir([1,2,3])) 
print( dir(dict())) 

#몫과 나머지를 tuple로 보낸다 
mok, nmg = divmod(5,3)
print(mok)
print(nmg)

for i, c in enumerate("Life is egg"):
    print(i,c)

result = eval('1+10+3')
print(result)

result = eval('(1+10)*2-3')
print(result)

a =[3,4,-1,2,9,8,7,12,15,21]
#음수만 filter 의 첫번째매개변수는 함수여야 한다 
#두번째 매개변수로 전달된 요소하나를 매개변수로 하고 반환은 ,True또는 False
def isPositive(x):
    if x>0:
        return True 
    return False 

poList = list(filter(isPositive, a))
print(poList)

#한번 만들어서 쓰고 버리는 함수인 람다를 사용하자
poList = list(filter(lambda x: x>0, a))
print(poList)

print(f"최대값 {max(a)}  최소값:{min(a)}")
print(pow(2,4))


#컴퓨터는 시간을 1970년1월1일을 기산점으로 초당 1씩 카운트
import datetime 
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5) 
print(day1)
print(day2)

day3 = day2 - day1 #timedelta 객체로 바뀌고 날짜를 갖고 있다
print(day3.days)

#말일까지 몇일이 남았는가?



