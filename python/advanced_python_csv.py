import csv
from collections import Counter
import re



facfile = open('faculty.csv')
faculty=csv.reader(facfile)
factable=[x for x in faculty][1:]
factrans = [list(x) for x in zip(*factable)]

emailsout=open(
    "/home/gavin/Metis/prework/dsp/emails.csv",
    mode='w', newline=)
for x in factrans[3]:
    emailsout.write(x)

emailsout.close()
