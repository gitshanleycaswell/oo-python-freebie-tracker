from .freebie import Freebie
from .dev import Dev

class Company:
    all = []
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Company.all.append(self)

    @property
    def freebies(self):
        companies_freebies = []
        for freebie in Freebie.all:
            if freebie.company.name == self.name:
                companies_freebies.append(freebie)
        return companies_freebies
    
    @property
    def devs(self):
        companies_devs = []
        for freebie in self.freebies:
            companies_devs.append(freebie.dev)
        return companies_devs

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(dev,self, item_name, value)
        if new_freebie not in Freebie.all:
            Freebie.all.append(new_freebie)

    @classmethod
    def oldest_company(cls):
        years = {}
        for company in Company.all:
            company_name = company.name
            founding_year = company.year
            years[company_name] = years.get(company_name, founding_year)

        oldest_company = min(years, key=years.get)
        return oldest_company