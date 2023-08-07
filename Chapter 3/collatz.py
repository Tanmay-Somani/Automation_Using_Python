def collatz(number):
    while True:
        if (number%2==0):
            number=number//2
            print(number)
        else:
            number=3*number+1
            print(number)
        if number==1:
            break
collatz(6)

