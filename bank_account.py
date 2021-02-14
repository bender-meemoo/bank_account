class bankAccount:
    def __init__(self, account, int_rate, balance):
        self.account = account
        self.int_rate = 0.02
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def interest_yield(self):
        self.balance += self.balance * self.int_rate
        return self
    def display_account_info(self):
        print(f"{self.account} interest yield is {self.int_rate} and the balance plus interest is {self.balance}")
        return self
    

account1 = bankAccount("account1", 0,0)
account2 = bankAccount("account2", 0,0)




account1.make_deposit(100).make_deposit(500).make_deposit(20).make_withdrawl(300).interest_yield().display_account_info()
account2.make_deposit(1000).make_deposit(40).make_withdrawl(40).make_withdrawl(30).make_withdrawl(35).make_withdrawl(20).interest_yield().display_account_info()
