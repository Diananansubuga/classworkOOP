# write a python programme that shows the use of modules and functions.
# create a module named "my_module" with a function called "addition".

def addition(a,b):
    return a+b

# function2
def multiplication(a,b):
    return a*b

# function3
def division(a,b):
    if b==0:
        print("Error")
    else:
        return a/b

# function4
def subraction(a,b):
    return a-b


# assign values to the function and call the function

addition1=addition(2,4)
print(f"The sum is {addition1}")

multiplication1=multiplication(2,3)
print(f"The product is {multiplication1}")

division1=division(2,0)
print(f"The quotient is {division1}")

subraction1=subraction(2,3)
print(f"The difference is {subraction1}")
    