#*
# cCount is a Script, that takes a Kaiju Output File and calculates how much was classified.
# Author: Jonas Hille
# This program was written in the course of my work on bioinformatics, in particular Nostoc Azolla, that was done as preparation for my bachelors thesis.
#*

def main():
    f = open("kaiju/TaxListMaker/kaiju_nr_a.out", "r") # reading in the Kaiju Output
    # initialize sums for the classified, unclassified and for all.
    u_sum = 0
    c_sum = 0
    complete_sum = 0

    # go through output and up the variables correspondingly.
    for x in f:
        if(x.split()[0] != 'U'):
            c_sum += 1
        else:
            u_sum += 1
        complete_sum += 1

    # sums get printed in absolute numbers and percentages.
    print('complete sum of reads are :', complete_sum)
    print('total classified :', c_sum)
    print('total unclassified :', u_sum)

    complete_sum /= 100
    c_sum /= complete_sum
    u_sum /= complete_sum

    print('1 percent of reads are :', complete_sum)
    print('total classified in percet :', c_sum)
    print('total unclassified in percent :', u_sum)  

    # file gets closed
    f.close()



if __name__ == "__main__":
    main()