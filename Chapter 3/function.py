def spam(dividify):
    try:
        return 40/dividify
    except ZeroDivisionError:
        print("Error: Invalid Argument")

print(spam(40),spam(0))
