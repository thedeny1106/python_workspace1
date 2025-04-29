#람다는 한줄짜리 함수, 함수를 쓰고 버린다. 
def add(x=0,y=0,z=0): #함수는 그 자체가 주소이다 
    return x+y+z  

myadd = add #myadd라는 변수에 add함수 주소가 들어간다 
print( myadd(3,4,5) )

#함수의 매개변수로 함수를 줄 수 있다. 

def myfunc(x, y, callback): #세번째인자가 callback - 함수주소를 받아옴 
    result = callback(x, y)
    print( x, y, result)

def add(x,y):
    return x+y 

myfunc(4,5, add) #함수주소를 전달한다 
myfunc(4,5, lambda x, y: x-y) #임시함수를 만든다. lambda로 시작해야 하고 이름은 
#없으며 두개의 매개변수를 가져야 한다. : 콜론뒤에는 함수의 내용을 기술하면 되고 return 은 생략이다

fucList = [ lambda x, y : x+y, 
            lambda x, y : x-y,
            lambda x, y : x*y,
            lambda x, y : x/y]
for fun in fucList:
    print( fun(9,7))

#앞에함수, 두번째인자에 iterable이 온다. 
#특정 조건에 맞는 데이터의 iterable타입을 반환한다. 

a = [1,2,3,4,5,6,7,8,9,10]
#첫번째 매개변수로 올 함수를 호출하는 호출자는 filter 임 
#매개변수가 하나이어야 하고, 반환값을 bool타입 True 또는 False이어야 함 
def isEven(n):
    return n%2==0

for i in filter( isEven, a):
    print(i)


for i in filter( lambda x:x%2==0, a):
    print(i)