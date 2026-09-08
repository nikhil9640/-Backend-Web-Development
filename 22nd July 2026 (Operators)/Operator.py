# 1. Variable increment
x = 10
x = x + 1
print(x)  # Output: 11

# 2. Basic logical AND
print(True and False)  # Output: False

# 3. Comparison and operator precedence (AND before OR)
# (True and True) or False -> True or False
print(10 >= 10 and 20 <= 30 or 30 <= 10)  

# 4. Negating the whole expression
# not(True)
print(not (10 >= 10 and 20 <= 30 or 30 <= 10))

# 5. Negating only the first condition
# not(True) or False -> False or False
print(not (10 >= 10 and 20 <= 30) or 30 <= 10)  

# 6. Combining NOT, AND, and OR
# not(True) or not(False) and (True or False)
# False or True and True -> False or True
print(
    not (10 >= 10 and 20 <= 30) or not (30 <= 10) and (True or (False))
)  

# 7. Similar to above, but with inner NOT
# False or True and (True or True) -> False or True and True
print(
    not (10 >= 10 and 20 <= 30) or not (30 <= 10) and (True or not (False))
)  

# 8. Simplified expression evaluation
# False or True and True
print(False or not (30 <= 10) and (True or not (False)))  

# 9. Final direct boolean evaluation
# False or (True and True) -> False or True
print(False or True and (True or not (False)))  