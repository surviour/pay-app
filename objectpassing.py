
class Category:
    ledger = []

    def __init__(self, name_category):
        self.name_category = name_category

    def Deposit(self, amount, description=""):
        d = dict()
        d["amount"] = amount
        d["description"] = description
        return d

class play:
    playList=[]
    def __init__(self):
        self.playList = []
    def printd(self):
        print(self.playList)
    def appendlist(self,dit):
        self.playList.append(dit)
        print(self.playList)

c=Category("food")
c1=Category("petrol")
p=play()
p.appendlist(c.Deposit(100))
p.appendlist(c1.Deposit(200))
 
