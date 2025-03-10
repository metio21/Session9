def hello(name, second):
q   2





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
