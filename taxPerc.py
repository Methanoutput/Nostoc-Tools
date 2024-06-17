#*
# taxPerc is a simple Script, that takes a Tax Report from NCBI and a Kaiju Output File and calculates the percentages for defined taxa.
# Author: Jonas Hille
# This program was written in the course of my work on bioinformatics, in particular Nostoc Azolla, that was done as preparation for my bachelors thesis.
#*

# TAX ID's:
#2 = Bacteria
#1117 = Cyanobacteria
#1161 = Nostocales
#551115 = Nostoc Azolla

import time #This is just here, because i wanted to take a look at my runtime.
start_time = time.time()



def main():
    f = open("kaiju/TaxListMaker/kaiju_nr_a.out", "r") # Reading in the Output from Kaiju. Change this to your corresponding file.
    l = open("kaiju/TaxListMaker/tax_report_nr.txt", "r") # Reading in the Tax Report from NCBI. Change this to your corresponding file.

    taxIDs = {} # create a dictionary for faster access than using a list, when we count
    # initialize a count variable for every species that we want to find. In my Case this 
    trichormus_sum = 0
    na_sum = 0
    nostocales_sum = 0
    cyano_sum = 0
    bac_sum = 0
    all_sum = 0

    # format the raw Input, so it easily facilitated
    for x in l:
        x = x.split("|")
        if(x[0] == '1\t' or x[0] == '2\t'):
            taxIDs[x[1].replace("\t", "")] = x[3]

    # go through input and up the counts, everytime 
    for i in f:
        i = i.split()
        if(i[0] == 'C' and i[2] != '1'):
            if('2' in taxIDs[i[2]]):
                bac_sum += 1
            if('1117' in taxIDs[i[2]]):
                cyano_sum += 1
            if('1161' in taxIDs[i[2]]):
                nostocales_sum += 1
            if('1164' in taxIDs[i[2]]):
                trichormus_sum += 1
            if('551115' in taxIDs[i[2]]):
                na_sum += 1
            all_sum += 1

    # calculate the percentage of each taxa relative to the complete sum of the output from kaiju
    one_perc = all_sum / 100
    na_percentage = na_sum / one_perc
    nostocales_percentage = nostocales_sum / one_perc
    cyanos_percentage = cyano_sum / one_perc
    bacis_percentage = bac_sum / one_perc

    # print the output
    print(" nostoc_azolla\t:" , na_sum, " |", na_percentage ,"|\n", 
          "nostocales\t:" , nostocales_sum, "|" , nostocales_percentage ,"|\n", 
          "cyanos\t\t:" , cyano_sum,"|", cyanos_percentage ,"|\n", 
          "bacis\t\t:" , bac_sum, "|" , bacis_percentage,  " |\n",
          "trichormus\t:" , trichormus_sum, "|" , trichormus_sum / one_perc, "|\n", 
          "alle\t\t:" , all_sum, "|" , "100")
    
    print("--- %s seconds ---" % (time.time() - start_time))

            
    # close all opened files
    l.close()
    f.close()



if __name__ == "__main__":
    main()