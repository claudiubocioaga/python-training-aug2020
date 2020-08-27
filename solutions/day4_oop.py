class BankAccount:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception('Insufficient funds!')
        self.balance -= amount


class Employee:
    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self.bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent):
        if percent not in (5, 10, 20):
            raise ValueError(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary

    def receive_salary(self):
        self.bank_account.deposit(self._salary)


if __name__ == '__main__':
    bank_acc = BankAccount('BRD', 100)  # create instance
    print('Initial balance:', bank_acc.balance)
    bank_acc.deposit(50)  # call deposit() method
    print('Balance after depositing 50:', bank_acc.balance)  # should be 150
    bank_acc.withdraw(70)  # call withdraw() method
    print('Balance after withdrawing 70:', bank_acc.balance)  # should be 80
    try:
        bank_acc.withdraw(100)  # should raise exception
    except Exception as ex:
        print(ex)
    print('Balance after trying to withdraw 100:', bank_acc.balance)

    emp = Employee("John Doe", bank_acc, 1000)
    emp.raise_salary(10)
    print(emp.salary)  # should print 1100
    emp.receive_salary()
    print(emp.bank_account.balance)  # should print 1180 (80 before salary + salary)
    emp.salary = 2000  # should raise exception (can't set attribute)

