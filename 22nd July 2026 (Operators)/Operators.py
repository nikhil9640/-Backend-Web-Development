# ==========================================
# 1. VARIABLE ASSIGNMENT & ARITHMETIC
# ==========================================
x = 10
x = x + 1
print("1. Variable increment x:", x)


# ==========================================
# 2. BOOLEAN LOGIC & EVALUATION
# ==========================================
print("2a. True and False:", True and False)

# Operator precedence: 'and' evaluates before 'or'
# (10 >= 10 and 20 <= 30) -> True and True -> True
# (30 <= 10) -> False
# True or False -> True
print("2b. Complex logic 1:", 10 >= 10 and 20 <= 30 or 30 <= 10)

print("2c. Complex logic 2:", not (10 >= 10 and 20 <= 30 or 30 <= 10))

print("2d. Complex logic 3:", not (10 >= 10 and 20 <= 30) or 30 <= 10)

print(
    "2e. Complex logic 4:",
    not (10 >= 10 and 20 <= 30) or not (30 <= 10) and (True or (False)),
)

print(
    "2f. Complex logic 5:",
    not (10 >= 10 and 20 <= 30) or not (30 <= 10) and (True or not (False)),
)

print("2g. Complex logic 6:", False or not (30 <= 10) and (True or not (False)))

print("2h. Complex logic 7:", False or True and (True or not (False)))

print("2i. Complex logic 8:", False or True and True)


# ==========================================
# 3. IF CONDITIONS
# ==========================================
print("\n--- Testing If Statements ---")

if 10 <= 29:
    print("Condition 1 matched: hello")

if 10 >= 29:
    print("Condition 2 matched: hello")  # Will not print

if not (10 >= 29):
    print("Condition 3 matched: hello")

if not (10 >= 29 and False):
    print("Condition 4 matched: hello")

if not (10 >= 29 and True):
    print("Condition 5 matched: hello")

if not (10 >= 29 and not (False)):
    print("Condition 6 matched: hello")

if not (10 >= 29 and not (False or True)):
    print("Condition 7 matched: hello")

if not (not (10 >= 29) or not (False or True)):
    print("Condition 8 matched: hello")

if not (not (not (10 >= 29) or not (False or True))):
    print("Condition 9 body:")
    print("hello")
    print("hiiii")
    print("abc")
    print("xyz")

print("BYE")


# ==========================================
# 4. IF / ELSE COMPARISONS
# ==========================================
print("\n--- Testing If/Else Comparisons ---")

a = 100
b = 20

if a > b:
    print("a IS GREATER")

A = 100
B = 200

# Using lower 'a' and 'b' defined above (100 > 20)
if a > b:
    print("A IS GREATER")

if a > b:
    print("a IS GREATER")
else:
    print("b IS GREATER")


# ==========================================
# 5. BOOLEAN IF / ELSE BLOCKS
# ==========================================
print("\n--- Testing Boolean Blocks ---")

if True:
    print("IF BLOCK")
else:
    print("ELSE BLOCK")

if not (True):
    print("IF BLOCK")
else:
    print("ELSE BLOCK")

if False:
    print("IF BLOCK")
else:
    print("ELSE BLOCK")

if 10 > 20:
    print("IF BLOCK")
else:
    print("ELSE BLOCK")


# Multi-line statement block 1
if True:
    print("IF BLOCK")
    print("ONE")
    print("TWO")
    print("THREE")
else:
    print("ELSE BLOCK")
    print("HELLO FROM ELSE BLOCK")
    print("HIII FROM ELSE BLOCK")
print("DONE")


# Multi-line statement block 2
if not (True):
    print("IF BLOCK")
    print("ONE")
    print("TWO")
    print("THREE")
else:
    print("ELSE BLOCK")
    print("HELLO FROM ELSE BLOCK")
    print("HIII FROM ELSE BLOCK")
print("DONE")


# ==========================================
# 6. NESTED VS INDEPENDENT IF STATEMENTS
# ==========================================
print("\n--- Testing Nested vs Independent Ifs ---")

# Nested condition
X = True
if X:
    print("Nested test - First block: Hello")
else:
    if not (not (X)):
        print("Nested test - Else block: bye")

# Sequential condition
if X:
    print("Sequential test - First if: Hello")
if not (not (X)):
    print("Sequential test - Second if: bye")