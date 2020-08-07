import time
import os

print("""
                 _               _     _           
                | |   ____      | |   | |          
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                   __/ |
                                             |___/       
      """)

print("textamina by root@ebby")
time.sleep(1)
print("THIS CODE ONLY WORKS ON LINUX")
time.sleep(1)
print("Getting Ready ...")
time.sleep(3)

while True:
    print("""
1. Editor
2. Exceptions - Problems          
3. EXİT
          """)
    option = int(input("Option : "))
    
    if option == 1:
        print("Preparing editor...")
        time.sleep(3)
        print("(exit - q - çıkış) to exit ...")
        print("if there's an error , go to Exceptions - Problems")
        time.sleep(2)       
        while True:
            text = input("TEXT : ")        
            if text == "çıkış" or text == "exit" or text == "q":
                break               
            else:
                os.system("figlet '{}' ".format(text)) 
          
    elif option == 2:
        print("what's wrong ?")
        print("1. Figlet not found !")
        print("2. Can't install figlet")
        error = int(input("Error : "))
        if error == 1:
            print("wait a sec , fixing ... ")
            os.system("apt install figlet")
            time.sleep(2)
            print("READY !!!")
        elif error == 2:
            print("Wait ...")
            source = "etc/apt/sources.list"
            with open(source,"w") as file:
                file.write("deb http://http.kali.org/kali kali-rolling main contrib non-free")
            time.sleep(2)
            os.system("apt update")
            time.sleep(2)
            print("READY !!!")
        else:
            print("Please select 1 or 2")
    elif option == 3:
        print("Goodbye !")
        time.sleep(1)
        break
    
    else:
        print("Please select 1 - 2 - 3")
    



