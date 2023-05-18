def fun():
    print("Welcome to GFG")
 
fun()

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

# -------------------------------------------------

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
 
print(calc(20))

# -----------------------------------------------------.

def f():
     
    # local variable
    s = "I love Geeksforgeeks"
    print(s)
 
 
# Driver code
f()


# This function uses global variable s
def f():
    print("Inside Function", s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

# ------------------------------------------

def shout(text):
    return text.upper()
  
def whisper(text):
    return text.lower()
  
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print (greeting) 
  
greet(shout)
greet(whisper)