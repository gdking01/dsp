import csv
from collections import Counter
import re



facfile = open('faculty.csv')
faculty=csv.reader(facfile)
factable=[x for x in faculty][1:]
factrans = [list(x) for x in zip(*factable)]
print(Counter(factrans[1]))
degrees=' '.join(factrans[1])

# CODE FOR Q1
patterndict = {'Ph\.?D\.?':'PhD',
    'B\.S\.Ed.':'B.S.Ed.',
    'JD':'JD',
    'M\.?S\.?':'MS',
    'MA':'MA',
    'MD':'MD',
    "MPH":"MPH",
    "Sc\.?D\.?":"ScD"}

for s in patterndict:
    print(str(patterndict[s]) + ":" +
    str(len(re.findall(s,degrees))))

# CODE FOR Q2
titlecounts = Counter(re.findall('.*Professor',x)[0] \
    for x in factrans[2])

for x in titlecounts.keys():
    print(x, titlecounts[x])

# CODE FOR Q3
for x in factrans[3]:
    print(x)

#CODE FOR Q4
domaincounts=Counter(re.findall('@.*$',x)[0] \
    for x in factrans[3])
for x,y in domaincounts.items():
    print(x,":",y)

facfile.close()
