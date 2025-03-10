#file reader
fp = open("text.txt", "r") # r is by default, so not really needed
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close file

#same thing with context manager
with open("text.txt", "r") as fp:
    print(fp.read())

print("read the file line by line")
line_number = 1 # starts counting for this
with open("text.txt", "r") as fp:
    for line in fp: # iterates over file to print file line by line
        print(f"{line_number}: {line}", end="") # ask file not to add new line
        line_number += 1


print("done printing")
print("done with the code")

#diary
#lets create a virtual diary
with open ("diary.txt", "a") as fp: # if this file does not exist, it will be created and a will append aka keep history
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q": # double == means equal to
            break
        fp.write(f"{text}\n") #\n make a new line


#function example
def greet():
    """
    Simple function that just prints hello
    :return:
    """
    print("Hello!")

def greet2(name):
    """
    simple function that greets a person
    :param name: the name of the person
    :return: none
    """
    print(f"Hello, {name}") # adds the name inputted in the def brackets

greet2("Jane")
greet2("Mary")


def special_op(a=1,b=1):
    """
    Special op is 10xaxb
    :param a: first number
    :param b: second number
    :return: value, 10a + b
    """
    return 10*a + b
    # or print(f"Your special value is {10*a + b}")

special_op(1,2)
print(special_op(10,9))
print(special_op())
print(special_op(a=9)) # excutes 91

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name} {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name(first_name = "John", last_name ="Doe"))
bond_greet(bondise_name())
