# -------------------------------------------------------------------
# 1. Basic Print Statements
# -------------------------------------------------------------------
print(123)       # (Integer)
print(123.456)   # (Float)
print("abc")     # (String)
print("ABC")     # (String)
print('abc')     #(Single quotes work the same as double quotes)
print('ABC')     

# Direct arithmetic inside print
print(10 + 20)   


# -------------------------------------------------------------------
# 2. Variable Assignment & Naming Conventions
# -------------------------------------------------------------------
x = 10 
y = 20
print(x + y)    

phn = 1234567890
print(phn)       

bank_account = 98761234567890  # Converted to standard snake_case

x = 10
x1 = 20
x2 = 30
x100 = 200
xabc = "abc"

print(xabc)      
print(x)         
print(x1)        
print(x2)        
print(x100)      

# String variables representing contact numbers
amma_jio = "1234567890"
nanna_airtel = "0987654321"

print(amma_jio)       
print(nanna_airtel)


# -------------------------------------------------------------------
# 3. Variable Reassignment & Identifier Rules
# -------------------------------------------------------------------
x = 10
y = 20
x = 30           # Reassigns x from 10 to 30
print(x)         

_1y = 20         # Variable names can start with an underscore
print(_1y)       

# Invalid identifier (hyphens are treated as subtraction operator):
# full-stack-expert = 10  # SyntaxError

# Naming style examples
full_stack_expert = 10      # Standard snake_case
innomatic_research_lab = 20 # Standard snake_case
print(innomatic_research_lab)

innomatic_research_lab_id = 1234567890
print(innomatic_research_lab_id)

full_name = "abcdef"        # snake_case
print(full_name)

full_name_camel = "abcdef"  # camelCase style
print(full_name_camel)


# -------------------------------------------------------------------
# 4. Data Types & Type Inspection
# -------------------------------------------------------------------
x = 10.65
print(x)         
print("x")      
print(type(x))   

x = "34.56"      # Reassigned to string
print(type(x))   


# -------------------------------------------------------------------
# 5. Arithmetic Operators
# -------------------------------------------------------------------
num1 = 10
num2 = 20
result = num1 + num2
print(result)    

print(num1 + num2)   # Addition: 30
print(num1 - num2)   # Subtraction: -10
print(num1 * num2)   # Multiplication: 200
print(num1 / num2)   # Floating point division: 0.5
print(num1 % num2)   # Modulus (Remainder): 10
print(num1 // num2)  # Floor division (Integer result): 0
print(num1 ** 3)     # Exponentiation (10^3): 1000
print(num2 ** 3)     # Exponentiation (20^3): 8000


# -------------------------------------------------------------------
# 6. Assignment & Compound Operators
# -------------------------------------------------------------------
# Sequence 1
x = 10
x = x + 10       # Equivalent to x += 10
print(x)         

# Sequence 2
x = 10
x = x + 10       # x becomes 20
x += 10          # x becomes 30
print(x)         

# Sequence 3
x = 10
x = x - 1        # x becomes 9
x *= 2           # x becomes 18
print(x)         

# Sequence 4
x = 10
x -= 1           # x becomes 9
print(x)         

# Sequence 5
x = 10
x *= 1           # x remains 10
print(x)        

# Sequence 6
x = 10
x *= 2           # x becomes 20
print(x)         


# -------------------------------------------------------------------
# 7. Comparison Operators
# -------------------------------------------------------------------
x = 10
y = 10
print(x == y)    

x = 20
y = 30
print(x == y)    

x = 10
y = 10
print(x != y)    
print(x > y)     
print(x >= y)    
print(x < y)     
print(x <= y)    


# -------------------------------------------------------------------
# 8. Logical Operators Truth Table (Reference)
# -------------------------------------------------------------------
print(False and False)  
print(True and False)  
print(False and True)    
print(True and True)   