from patternmodel import *

filename = "/media/hdevos/5452B30B52B2F0BA/MA Thesis/patternmodels/strafrecht_patternmodel.tab"

pm = Patternmodel()
pm.read_patternmodel(filename)

for key, val in pm.entries.items():
    print('{}\t{}'.format(key, val))

print ()