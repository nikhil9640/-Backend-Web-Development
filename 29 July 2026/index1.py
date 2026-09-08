# ==========================================
# 1. BASICS & STRING FORMATTING
# ==========================================
print("Hello World")

course = "FSD"
location = "JNTU"
print("I am Learning", course, "at the Location", location)

a, b, c, d = 10, 20, 30, 40
# Concatenation vs F-Strings
print("The sum of", a, "and", b, "and", c, "and", d, "is:", a + b + c + d)
print(f"The sum of {a} and {b} and {c} and {d} is {a + b + c + d}")

# Min / Max functions
print("Max value:", max(10, 20, 30, 40))
print("Min value:", min(10, 20, 30, 40))


# ==========================================
# 2. TYPE CASTING & DIGIT EXTRACTION
# ==========================================
# Type Casting (Float to Int)
z = 123.23432
u = int(z)
print(f"Original: {z} ({type(z)}), Casted: {u} ({type(u)})")

# Extracting and summing digits of a 3-digit number (876)
num1 = 876
digit_last = num1 % 10
digit_middle = (num1 % 100) // 10
digit_first = num1 // 100

digit_sum = digit_last + digit_middle + digit_first
print(f"Digits of {num1}: {digit_first}, {digit_middle}, {digit_last}")
print(f"Sum of digits: {digit_sum}")

# Extracting digits using floor division and modulus
num2 = 4652
print("Extracting digits for 4652:")
print(num2 % 10)
print((num2 % 100) // 10)
print((num2 % 1000) // 100)
print(num2 // 1000)


# ==========================================
# 3. LOOPS & CONDITIONALS
# ==========================================
# Print Even numbers between 1 and 10
print("\n--- Even Numbers (1-10) ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Print Odd numbers between 1 and 10
print("\n--- Odd Numbers (1-10) ---")
for j in range(1, 11):
    if j % 2 != 0:
        print(j)

# Check Even/Odd status for range 1 to 10
print("\n--- Even/Odd Check ---")
for i in range(1, 11):
    if i % 2 == 0:
        print("EVEN", i)
    else:
        print("ODD", i)

# Logical Operators in conditions (Range 1-10)
print("\n--- Numbers <= 5 OR >= 7 ---")
for j in range(1, 11):
    if j <= 5 or j >= 7:
        print(j)

# Nested Conditions: Even numbers between 50 and 60
print("\n--- Even Numbers between 50 and 60 ---")
for i in range(1, 101):
    if 50 <= i <= 60:
        if i % 2 == 0:
            print(i)


# ==========================================
# 4. LOOP CONTROL STATEMENTS (BREAK)
# ==========================================
# Loop stops when i equals 5
print("\n--- Break on i == 5 ---")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Loop stops immediately because (i <= 5) is True on the first iteration (i=1)
print("\n--- Break on i <= 5 (Triggers on first run) ---")
for i in range(1, 11):
    if i <= 5:
        break
    print(i)

# Loop runs until i reaching 5 (i >= 5 triggers break)
print("\n--- Break on i >= 5 ---")
for i in range(1, 11):
    if i >= 5:
        break
    print(i)

# Boolean evaluation: (i >= 5 and False) is always False, so break never hits
print("\n--- Break with 'and False' condition (Runs full loop) ---")
for i in range(1, 11):
    if i >= 5 and False:
        break
    else:
        print(i)