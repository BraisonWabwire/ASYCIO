# Args- used when a function is returning multiple arguments

# Function to iterate numbers
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,3,4))

# Function to display someones name
def display_name(*args):
    for name in args:
        print(f"my name is:{name}")

display_name("braison","brian","newton","bonface","elijah")

#kwargs- allows one to pass multiple key word arguments
def print_adress(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

print_adress(
    street='jomo kenyatta',
    zip='20100',
    state='nakuru',
    country='kenya'
)



