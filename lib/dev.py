from .freebie import Freebie

class Dev:
    def __init__(self, name):
        self.name = name

    @property
    def freebies(self):
        devs_freebies=[]
        for freebie in Freebie.all:
            if freebie.dev == self:
                devs_freebies.append(freebie)
        return devs_freebies
    
    @property
    def companies(self):
        devs_companies = []
        for freebie in self.freebies:
            devs_companies.append(freebie.company)
        return devs_companies
    
    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False
    
    def give_away(self, dev, freebie):
        if freebie == freebie:
            freebie.dev = dev
        else:
            return None
