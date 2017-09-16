import csv
from collections import Counter
import re



facfile = open('faculty.csv')
faculty=csv.reader(facfile)
factable=[x for x in faculty][1:]
factrans = [list(x) for x in zip(*factable)]

facdict1 = {}
for x in factable:
    surname = re.findall(" [^ ]*$", x[0])[0][1:]
    if surname in facdict1:
        facdict1[surname].append([x[1],x[2][:-17],x[3]])
    else:
        facdict1[surname]=[[x[1],x[2][:-17],x[3]]]

for x in range(3):
    print(list(facdict1.items())[x])

#Next question

facdict2 = {}
for x in factable:
    surname = re.findall(" [^ ]*$", x[0])[0][1:]
    firstname = re.findall("^[^ ]* ", x[0])[0][:-1]
    facdict2[(firstname, surname)] = [x[1],x[2][:-17],x[3]]

for x in range(3):
    print(list(facdict2.items())[x])

for x in facdict2.keys():
    print(x)

facfile.close()
