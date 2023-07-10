import ipdb
from lib import *

#code here
c1 = Company("Facebook", "2010")
c2 = Company("Google", "2002")
c3 = Company("Flatiron", "2015")

d1 = Dev("Shanley")
d2 = Dev("Steven")

f1 = Freebie(d1, c1, "Hat", "20")
f2 = Freebie(d2, c2, "Nice Tequila", "200")
f3 = Freebie(d1, c2, "Baseball", "50")
f4 = Freebie(d2, c3, "Whiskey", "200")



ipdb.set_trace()