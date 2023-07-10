
class Freebie:
    all=[]
    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company
        self.item_name = item_name
        self.value = value
        Freebie.all.append(self)

    
