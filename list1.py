
questions = ["This is Delhi? \n", "This is Paris ?\n", "This is London ? \n"]
answer = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

questions = ["This is Delhi? \n", "This is Paris ?\n", "This is London ? \n"]
answers = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# open a file to write to
with open("questions.txt", "w") as file:
    for question, answer in zip(questions, answers):
        file.write("Question: {}\n".format(question))
        file.write("Answer: {}\n\n".format(answer))

# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile11.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello , zzzzzzzzzz,\n gggggggggg\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile11.txt', 'r')
print(file1.read())
file1.close()