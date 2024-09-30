#Fill the comments
#modify the scr code if possible!
import random
import string

def generatePassword(length=12,useSpecial=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specialChars = string.punctuation if useSpecial else ' '
    allChars = lowercase+uppercase+digits+specialChars
    password = ''.join(random.choice(allChars) for i in range(length))
    return password
def main():
    length_pass = input("Enter your desired length of password (E.g. 12): ")
    length = int(length_pass) if length_pass else 12
    useSpecial = input("Do you want to use special chars in password(E.g. @,#): ").strip().lower() == "yes" or "y"
    password = generatePassword(length,useSpecial)
    print("Generated Password: ",password)
if __name__ == "__main__":
    main() 

