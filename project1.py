import random

def generatePassword(pwlength):
    alphabet  = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwlength:
        password = ""
        for j in range(i):
            next_alphabet_index= random.randrange (len(alphabet))
            password= password + alphabet[next_alphabet_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password)
    return passwords

def replaceWithNumber(pword):
    for i in range(random.randrange(1,7)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] +str(random.randrange(10)) +pword[replace_index+1:]
        return pword

def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,7)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index]+ pword[replace_index].upper() + pword[replace_index+1:]
        return pword

def main():
    numPasswords = int(input("Choose your desirable number of passwords do you want to generate?\n"))
    print("Generating"+str(numPasswords)+"passwords")
    passwordLengths = []
    print("Minimum length of password is 7")
    for i in range(numPasswords):
        length = int(input("Choose the length of password #"+str(i+1)+" "))
        if length<7:
            length = 7
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #"+str(i+1)+"=" + Password[i])
main()

