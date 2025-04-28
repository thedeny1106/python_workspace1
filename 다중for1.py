
#for문안에서 또  for문이 작동하는 경우다 
#외부의 루프가 m 번 돌고, 내부 루프가 n번 돌면 m * n번 수행을 한다. 
#가급적 2중 for문까지만 동작하게 해야 한다. 
for i in range(1,6):
    for j in range(1,6):
        print( f"i={i} j={j}")


#문제1. 이중 for문 사용해서 1~100 까지 출력 한줄에 10개씩 출력하기 
k=1 
for i in range(0,10):
    for j in range(0, 10):
        print(f"{k}", end="\t")
        k+=1
    print() #줄바꿈 

#문제2. 이중 for문 
#  1  = 1
#  1 + 2  = 3
#  1 + 2  + 3 = 6
#  1 + 2  + 3 + 4 = 10
#  1 + 2  + 3 + 4 + 5= 15 .........

for i in range(1, 11):
    sum=0
    for j in range(1, i+1):
        if j<i:
            print(j, end= " + ")
        else:
            print(j, end= " = ")
        sum += j 
    print (sum)
