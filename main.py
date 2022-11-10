# budget app
class Category:
    def __init__(self, name_category):
        self.name_category = name_category
        self.total = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})

    def __str__(self):
        header = self.name_category.center(30, "*")
        print(header)
        for item in self.ledger:
            amount = '%.2f' % item["amount"]
            desc = (item["description"][:28-(len(amount))]+"..") if len(
                item["description"]) > 28-(len(amount)) else item["description"]
            space = " "*(30-(len(desc)+len(amount)))
            txt = f"{desc:<}{space}{amount:>}"
            print(txt)
        print("Total: "+"%.2f" % self.total)

    def withdraw(self, amount, description):
        if (self.check_funds(amount)):
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, instance):
        if (self.check_funds(amount)):
            self.total -= amount
            self.ledger.append(
                {"amount": -amount, "description": "Transfer to "+str(instance.name_category)})

            instance.total += amount
            instance.ledger.append(
                {"amount": amount, "description": "Transfer form "+str(instance.name_category)})
            return True

        else:
            return False

    def get_balance(self):
        return self.total

    def check_funds(self, amount):
        if (amount > self.total):
            return False
        else:
            return True


food = Category("food")
car = Category("car")
bike = Category("Bike")
food.deposit(100, "initial desposit")
print(food.ledger)
print(food.total)
food.deposit(900, "bonus")
print(food.total)
print(food.ledger)
food.withdraw(30, "lunch")
print(f"total: {food.total} and\nledger is: {food.ledger}")
print(food.get_balance())
food.transfer(200, car)
print(food.ledger)
print(car.ledger)
car.transfer(10, bike)
print(bike.ledger)
food.__str__()
