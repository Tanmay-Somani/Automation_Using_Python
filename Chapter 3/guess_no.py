import random 
print("I am thinking of a number between 1 and 20.")
instance=random.randint(1,20)
print(instance)
cnt=0
while True:
    print("Take a guess")
    choice=int(input())
    if instance >choice:
        print("your guess is too low")
    elif instance < choice:
        print("your guess is too high")
    elif instance==choice:
        print("Goodjob! you guessed my number in "+str(cnt)+" guesses.")
        break
    cnt+=1