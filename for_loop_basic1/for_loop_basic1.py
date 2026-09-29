for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if (i%10==0):
        print(str(i) +"Coding Dojo")
    elif  (i%5==0):
        print(str(i) + "coding")


total = 0
for i in range(0, 500001):
    if i % 2 == 1:
        total += i
print(total)

#Countdown by Forus

for i in range(2018, 0, -4):
    print(i)


    #Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)