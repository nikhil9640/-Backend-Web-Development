
for i in range(1,11):
    if(i <= 8 and i%2 == 0):
        break
    elif(True):
        print(i)
    else:
        break


for i in range(1,11):
    if(i <= 8 and i%2 == 0):
        print(i)
    elif(True):
        print(i)
    else:
        break

x = True
for i in range(1,11):
    if(i <= 8 and i % 2 == 0):
        print(i)
    elif(x):
        print(i)
    else:
        break

x = True
for i in range(1,11):
    if(i <= 8 and i % 2 == 0):
        print(i)
        x = False
    elif(x):
        print(i)
    else:
        break

for i in range(1,11):
    if(i <= 8 and i % 2 == 0):
        print(i)
    elif(False):
        print(i)
    else:
        break


x= 10

print ("hello",x)

for i in range(1,11):
    print("hello ", i)
