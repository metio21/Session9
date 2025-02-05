#lets create a virtual diary
with open ("diary.txt", "a") as fp: # if this file does not exist, it will be created and a will append aka keep history
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q": # double == means equal to
            break
        fp.write(f"{text}\n") #\n make a new line


