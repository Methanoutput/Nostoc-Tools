#*
# listMaker is a Script, that takes a Kaiju Output File and creates a txt file containing all unique taxID's.
# Author: Jonas Hille
# This program was written in the course of my work on bioinformatics, in particular Nostoc Azolla, that was done as preparation for my bachelors thesis.
#*


def main():
    f = open("kaiju/TaxListMaker/kaiju_nr_a.out", "r") # reading in kaiju Output
    w = open("listmakerOutputnr.txt", "w") # creating output file
    idList = [] # creating a list for the id's
    for x in f: # go through the file and add the corresponding number uniquely.
        if(x.split()[2] != '0' and x.split()[2] not in idList):
            idList.append(x.split()[2])
            w.write(x.split()[2])
            w.write("\n")
    print(idList) # print the list. If your list will be longer, you should comment this out or your terminal will be bloated.

    # files get closed
    w.close()
    f.close()



if __name__ == "__main__":
    main()