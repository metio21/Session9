fp = open("text.txt", "r") # r is by default, so not really needed
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close file
