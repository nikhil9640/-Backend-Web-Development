# Comparison and logical operations
x = 10
y = 10

x = 110
y = 101

print(x < 10 and y > 10)
print(x < 10 and y < 10)
print(x < 10 and y > 10)
print(x > 10 and y > 10)

x = 110
y = 101

print(not (not (x > 10)) or y > 10)