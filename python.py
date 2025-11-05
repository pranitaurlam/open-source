def calculator(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b
    elif c=="**":
        return a**b
    elif c=="//":
        return a//b
    else:
        return "Unsupported operator"
print(calculator(2,4,"-"))

class bankAccount:
    __accountNumber = None
    __accountHolder = None
    __balance = None
    def __init__(self, accountNumber, accountHolder):
        self.__accountNumber = _____________
        self.__accountHolder = _____________
        self.__balance = _
    def deposited(self, _____):
        bankAccount.__balance += ______
        print(f"Deposited: ${bankAccount.__balance}")
    def withdrawl(self, _____):
        bankAccount.__balance -= ______
        print(f"Deposited: ${bankAccount.__balance}")
    def getAccountInfo(self):
        print(f"Account Number: {__________}")
        print(f"Account Holder: {}")
        print(f"Balance: {}")
bankObj = bankAccount(12212, _____)
bankObj._____(1000)
bankObj._____(500)
bankObj.getAccountInfo()