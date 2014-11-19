# CMA hit machine
# matt dargen

import random


def main():

    #initializing junk
    lines = open("country_lines.txt",'r')
    r = random.Random()
    min_len = 5

    #contructing ngrams
    ngrams = lines.read().split()
    ngrams = zip(ngrams,ngrams[1:],ngrams[2:])

    print("Press enter for a verse")
    while True:
        raw_input()

        verse = []
        line = ""
        i = 0
        while i < 4:
            ng = r.choice([x for x in ngrams if "<l>" not in x])
            while ng[2] != "<l>":
                ng = r.choice([x for x in ngrams if x[0] == ng[1] and x[1] == ng[2]])
                line += ng[0] + " "
            line += ng[1]
            if len(line.split()) < min_len:
                line = ""
                continue
            else:
                verse.append(line)
                line = ""
                i += 1

        #print verse
        for l in verse:
            print(l)

main()
