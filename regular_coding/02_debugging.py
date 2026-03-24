

# try / catch

try:
    print("Trying to divide by zero!")
    x = 1 / 1
    print(x)
    print("universe just blew up!")
except ZeroDivisionError as ex1:
    print("Exception caught! Error message:")
    print(ex1)
except ValueError as ex2:
    print(ex2)
except Exception as ex3:
    print(ex3)
except AttributeError as ex4:
    # Because Exception is caught earlier, we won't get here in this AttributeError exception.
    print(ex4)
finally:
    # This "finally" block runs no matter what.
    print("Finally")

print("And everything continues as it was.")
print("End of file.")

