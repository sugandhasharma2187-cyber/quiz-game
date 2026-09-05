file = open("question.txt","r")
questions = []

for content in file:
    questions.append(content.strip())

question = questions.pop(0).split("|")

print(question[0])
print(question[1])
print(question[2])
print(question[3])
print(question[4])
print(question[5])