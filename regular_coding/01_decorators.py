
USER_AUTHENTICATED = False

def my_decorator(func):
    def wrapper():
        print("This happens before my function runs!")
        func()
        print("After the function runs!")

    return wrapper

def is_logged_in(func):
    def wrapper():
        if USER_AUTHENTICATED:
            func()
        else:
            print("Cannot check balance, user is not authenticated!")
    return wrapper

@is_logged_in
def check_balance():
    print(3000)


# @my_decorator
# def check_balance():
#     print(3000)

USER_AUTHENTICATED = True
check_balance()

# var1 = my_decorator(check_balance)
# var1()












