
f = open("정수.txt", "r")
lines = f.readlines() 
sum=0
for line in lines:
    if "\n" in line:
        line = line[:len(line)-1]
    print(line)    
    sum += int(line)
f.close()

print("평균", sum/len(lines))

