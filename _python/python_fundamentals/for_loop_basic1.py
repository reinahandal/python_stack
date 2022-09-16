# basic
for i in range(0,151):
    print(i)

# multiples of 5
for x in range(5,1000):
    if x%5 == 0:
        print(x)

# counting the dojo way
for i in range(1,100):
    if i%10 == 0:
        print("Coding")
    elif i%5 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Whoa that sucker's huge
sum = 0
for i in range(0,500000):
    if i%2 != 0:
        sum += i
print(sum)

# countdown by fours
for i in range(2018,-1,-4):
    print(i)

# flexible counter
lowNum = 2
highNum = 20
mult = 3
for i in range(lowNum,highNum):
    if i%mult == 0:
        print(i)