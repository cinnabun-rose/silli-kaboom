import random
import os
import time

def main():
    un = input("Please set a username: ")
    print(f"Hello, {un}, and welcome to Cinnamon's super cool silly game!")
    time.sleep(2)
    print("To summarize, you have to choose wether you want to play or not and good luck!")
    time.sleep(2)
    input_game()

def input_game():
    answer = input("Do you want to play (Y/N): ")
    answer_c = answer.capitalize()
    if answer_c == "Y":
        choice = random.randint(1,2)
        if choice == 1:
            print("Lucky you! You're safe.")
            input_game()
        elif choice == 2:
            print("Say bye to... Uh. Something? I dunno")
            for i in range(5):
                print("...")
                time.sleep(1)
            time.sleep(3)
            
            # Well, over here there should be a os.rmdir
            # pointing to System 32, but I still don't know
            # how to do that.
            
            print("Oh yes! Your whole thing-")
            start_path='/'
            for dirpath, dirnames, filenames in os.walk(start_path):
                print(dirpath)
            print("Done :3")
        else:
            print("You should not be able to see this... Uh, error 420?")
    
    elif answer_c == "N":
        print("Okay!")
        print("Game over.")
        
    else:
        print("Error 420. Eh, joking - This is not a valid answer.")
        input_game()
            
if __name__ == ("__main__"):
    main()
