#Why are you looking at my guts? Hahaha. Just kidding, it's nice of you to look at my code. This took wayyyyy longer to make then i expected.

import random
import hashlib

#Loop in case you guess right or wrong, the game will restart with a new hash.
while (True):

#Here we get a random password from a part of a rockyou.txt(There is 230 passwords in this list).
    with open('rys.txt') as pw:
        password = pw.read()
        rsp = list(map(str, password.split()))
        unhashed = (random.choice(rsp))

#Here we hash the password.
    def ch1():
        global hex_digest
        hash_object = hashlib.sha256(unhashed.encode())
        hex_digest = hash_object.hexdigest()
    def ch2():
        global hex_digest
        hash_object = hashlib.md5(unhashed.encode())
        hex_digest = hash_object.hexdigest()
    def ch3():
        global hex_digest
        hash_object = hashlib.sha256(unhashed.encode())
        hex_digest = hash_object.hexdigest()
    def ch4():
        global hex_digest
        hash_object = hashlib.sha1(unhashed.encode())
        hex_digest = hash_object.hexdigest()

#Choice of random hash moduls
    funcions = "ch1","ch2","ch3","ch4"
    choice = (random.choice(funcions))
    if choice == "ch1":
        ch1()
    elif choice == "ch2":
        ch2()
    elif choice == 'ch3':
        ch3()
    elif choice == 'ch4':
        ch4()       

#Print
    hash = (ch1 or ch2 or ch3 or ch4)
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