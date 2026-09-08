# Loops and Conditional Statements Examples

for i in range(1,11):
    if(i>= 6):
        print(i)

for j in range(1,11):
    if(j > 4 and j < 8):
        # print(j)
        break
    if(j == 8):
        print(j)

for i in range(1,11):
    if(i == 8):
        print(i)
    if(i == 8):
        break

for i in range(1,11):
    if(i == 8):
        print(i)
    else:
        break


for i in range(1,11):
    if(i <= 8):
        print(i)
    else:
        break



for i in range(1,11):
    if(i <= 8 and i%2 == 0):
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


for i in range(1,11):
    if(i <= 8 and i%2 == 0):
        break
    elif(True):
        print(i)
    else:
        break
