#Esercizio 1
'''
print("Inserisci un numero")
num1=int(input())
print("Inserisci il secondo numero")
num2=int(input())

print("Il risultato é " + str(num1+num2))

'''

#Esercizio 2

'''
string = "Federico"
if len(string) < 2:
    print(" ")
elif  len(string)==2:
    print(string[0]+string[1])
elif len(string)==3:
    print(string[0]+string[1]+string[2])
else:
    print("Il risultato e': " + string[0]+string[1]+string[len(string)-2]+string[len(string)-1])
'''

#Esercizio 3
given_list = ["go_home", "study", "eat", "sleep"]

flag=True
while flag==True:
    print('''1. insert a new task
            2. remove a task (by typing its content, exactly)
            3. show all existing tasks
            4. close the program''')


    print("Insert a command: ")
    command = int(input())

    if command == 1:
        print("New task")
        new_task = input()
        given_list.append(new_task)

    elif command == 2:
        print("Type a content")
        content = input()
        for content in given_list:
            given_list.remove(content)

    elif command == 3:
        for task in given_list:
            print(task)

    elif command == 4:
        flag = False


