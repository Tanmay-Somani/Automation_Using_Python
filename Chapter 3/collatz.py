def collatz(number):
    while True:
        if number%2==0:
            a=number//2
            print(a)
        else:
            a=3*number+1
            print(a)
        if a==1:
            break

