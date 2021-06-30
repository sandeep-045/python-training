from time import sleep
import random
com=["snake","water","gun"]
print("Game begins in.....")
sleep(1)
print("3 ")
sleep(1)
print("2 ")
sleep(1)
print("1",)
p_score=0
c_score=0
while(p_score!=2 and c_score!=2):
    p_choice=input("Enter your choice:")
    number=random.randint(0,2)
    c_choice=com[number]
    if p_choice==c_choice:
        print("Oops It's a tie Computer chose the same")
    else:
        if p_choice=="snake":
            if c_choice=="water":
                p_score+=1
                sleep(1)
                print("Player Wins the round Computer chose {}".format(c_choice))
            elif c_choice=="gun":
                c_score+=1
                sleep(1)
                print("Computer Wins the round Computer chose {}".format(c_choice))
        elif p_choice=="water":
            if c_choice=="gun":
                p_score+=1
                sleep(1)
                print("Player Wins the round Computer chose {}".format(c_choice))
            elif c_choice=="snake":
                c_score+=1
                sleep(1)
                print("Computer Wins the round Computer chose {}".format(c_choice))
        elif p_choice=="gun":
            if c_choice=="snake":
                p_score+=1
                sleep(1)
                print("Player Wins the round Computer chose {}".format(c_choice))
            elif c_choice=="water":
                c_score+=1
                sleep(1)
                print("Computer Wins the round Computer chode {}".format(c_choice))
    sleep(0.4)
    print(f"Player Score:{p_score}  Computer Score:{c_score}")
    sleep(0.4)

if p_score==2:
    print("Player wins")
else:
    print("COmputer wins")