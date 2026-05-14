import random
import hashlib
#Loop in case you guess wrong, the game will restart with a new hash.
while (True):
#Here we get a random password from a part of a rockyou.txt(There is 230 passwords in this list).
    with open('rys.txt') as pw:
        password = pw.read()
        rsp = list(map(str, password.split()))
        unhashed = (random.choice(rsp))

#Here we hash the password.
    hash_object = hashlib.sha256(unhashed.encode())
    hex_digest = hash_object.hexdigest()
#Print 
    print("Simple game of capture a hash. Decode the hash to win a game")
    print("To exit the game type 0.")
    print(f"Hash: {hex_digest}")
    awnser = input("What is the password?:")

#Check if the passwrod is correct.
    if awnser == "0":
        print("Sorry to see you go. :(")
        break
    elif awnser == unhashed:
        print("Good job, you won!!!")
    elif awnser != unhashed:
        print("Nice try but your guess is wrong. Goodluck next time.")