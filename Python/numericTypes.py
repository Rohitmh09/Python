"""
PYTHON NUMERIC - TREE STRUCTURE
================================
 
Numeric
├── Types
│   ├── type()
│   ├── int()
│   ├── float()
│   └── complex()
│
├── Math Operators
│   ├── 3 + 2
│   ├── 3 - 2
│   ├── 3 * 2
│   ├── 3 / 2
│   ├── 3 // 2
│   ├── 3 % 2
│   └── 3 ** 2
│
├── Rounding
│   ├── abs()
│   ├── round()
│   ├── math.ceil()
│   ├── math.floor()
│   └── math.trunc()
│
├── Advanced Math
│   ├── math.sqrt()
│   ├── math.sin()
│   ├── math.cos()
│   └── math.log()
│
├── Random
│   ├── random.random()
│   └── random.randint()
│
└── Validation
    ├── is_integer()
    └── isinstance()
"""


import math
import random


# ============================================================
# 1. TYPES
# ============================================================
# These tell you what "kind" of number something is, or convert
# a value into a specific number type.
 
print("----- TYPES -----")
 
# type() -> tells you the data type of a value (like asking "what are you?")
print(type(5))          # <class 'int'>   -> whole number
print(type(5.0))        # <class 'float'> -> decimal number
 
# int() -> converts a value into a whole number (removes decimal part)
print(int(9.8))         # 9  (just cuts off .8, doesn't round)
 
# float() -> converts a value into a decimal number
print(float(7))         # 7.0
 
# complex() -> creates a complex number (has a real + imaginary part)
# Rarely used unless you're doing advanced math/engineering.
print(complex(2,3))    # (2+3j) #if single number like complex(2) ==> (2+j0)

 
  
# ============================================================
# 2. MATH OPERATORS
# ============================================================
# Basic symbols used to do arithmetic between numbers.
 
print("\n----- MATH OPERATORS -----")
 
print(3 + 2)   # Addition       -> 5
print(3 - 2)   # Subtraction    -> 1
print(3 * 2)   # Multiplication -> 6
print(3 / 2)   # Division       -> 1.5   (always gives decimal)
print(3 // 2)  # Floor Division -> 1     (division, then drop decimal)
print(3 % 2)   # Modulus        -> 1     (gives the REMAINDER of division)
print(3 ** 2)  # Exponent       -> 9     (3 raised to the power of 2)


 
# ============================================================
# 3. ROUNDING
# ============================================================
# Different ways to round or clean up numbers.
 
print("\n----- ROUNDING -----")
 
# abs() -> gives the "absolute value" (removes negative sign)
print(abs(-3))         # 3
 
# round() -> rounds to the nearest whole number (or given decimal places)
print(round(4.6))      # 5
print(round(4.567, 2)) # 4.57  (round to 2 decimal places)
 
# math.ceil() -> always rounds UP to the next whole number
print(math.ceil(4.1))  # 5
 
# math.floor() -> always rounds DOWN to the previous whole number
print(math.floor(4.8)) # 4
 
# math.trunc() -> just chops off the decimal part (no rounding logic)
print(math.trunc(4.3)) # 4
print(math.trunc(-4.9))# -4  (trunc doesn't round toward smaller, it just cuts)


# ============================================================
# 4. ADVANCED MATH
# ============================================================
# These come from Python's built-in "math" module.
 
print("\n----- ADVANCED MATH -----")
 
# math.sqrt() -> square root of a number
print(math.sqrt(9))   # 4.0
 
# math.sin() -> sine of an angle (angle must be in radians)
print(math.sin(0))     # 0.0
 
# math.cos() -> cosine of an angle (in radians)
print(math.cos(0))     # 1.0
 
# math.log() -> natural logarithm (log base e) of a number
print(math.log(1))     # 0.0
print(math.log(100, 10))  # 2.0  (log base 10 of 100)
 
# ============================================================
# 5. RANDOM
# ============================================================
# Used to generate random numbers. Comes from the "random" module.
 
print("\n----- RANDOM -----")
 
# random.random() -> gives a random decimal number between 0.0 and 1.0
print(random.random())        # example: 0.7623
 
# random.randint(a, b) -> gives a random WHOLE number between a and b (inclusive)
print(random.randint(1,20))  # example: 7



# ============================================================
# 6. VALIDATION
# ============================================================
# Used to check facts about a number or a variable.
 
print("\n----- VALIDATION -----")
 
# is_integer() -> checks if a float value is actually a whole number
print((4.0).is_integer())   # True
print((5.6).is_integer())   # False
 
# isinstance() -> checks if a variable belongs to a certain type
x = 2
print(isinstance(x,int))     # True | if 2.0 not full integer so its False it needed full integer format 3,56,22,1... etc
print(isinstance(x, float))   # False