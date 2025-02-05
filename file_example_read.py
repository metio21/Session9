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
