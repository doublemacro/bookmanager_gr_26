
class BankAccount:
    bank_name = "ING"

    def __init__(self, owner):
        self.owner = owner
        # __balance is now private. Can only be accessed from inside the class, its methods and properties
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if BankAccount.is_valid_amount(value):
            self.__balance = value
        else:
            print("Error, parameter must be a postive integer!")

    # methods, class methods, static methods.
    # methods schimba si depind de instantele clasei
    # class methods schimba atribute ale clasei in sine, si tin doar de clasa, nu de instantele ei
    # static methods sunt mai independente, nu tin de vreo proprietate a clasei sau a instatelor ei. Deseori contine logica de validare, de conversie, sau orice logica care tine de clasa, dar nu de proprietatile ei in mod direct.

    @classmethod
    def change_bank_name(cls, name):
        # BankAccount.bank_name = name
        # cls se refera la clasa in sine, deci in cazul asta la BankAccount.
        cls.bank_name = name

    @staticmethod
    def is_valid_amount(amount):
        if isinstance(amount, int) and amount >= 0:
            return True
        else:
            return False

    # def set_balance(self, param1):
    #     if isinstance(param1, int) and param1 >= 0:
    #         self.__balance = param1
    #     else:
    #         print("Error, parameter must be a postive integer!")


BankAccount.change_bank_name("BNR")
adrian_ing = BankAccount("Adrian")
# adrian_ing.set_balance(100)
print(adrian_ing.balance)
print(adrian_ing.bank_name)

adrian_ing.balance = 100

print(adrian_ing.balance)

cont_doi = BankAccount("Matei")
cont_trei = BankAccount("Luca")
cont_doi.balance = 300
print(cont_doi.balance)
print(cont_trei.balance)

print(cont_trei.bank_name)

def harababura():
    print("Avadakadavra.")

print(BankAccount.is_valid_amount(300))
