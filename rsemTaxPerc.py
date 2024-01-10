def main():
    isoforms = open("Nostoc-Data/sample_a.isoforms.results", "r") #number 6 is index for tpm
    matches = open("Nostoc-Data/matches_v218_a_taxon", "r")
    tr2tax = {}
    calculated = {}

    not_there = 0
    there = 0

    nostoc_azolla = 0
    trichormus = 0

    tpm_nostoc_azolla = 0
    tpm_trichormus = 0
    
    for x in matches:
        x = x.split()
        tr2tax[x[0]] = x[12]
        calculated[x[0]] = False
    for x in isoforms:
        x = x.split()
        if(x[0] in calculated):
            if('551115' in tr2tax[x[0]]):
                nostoc_azolla = nostoc_azolla + 1
                tpm_nostoc_azolla = tpm_nostoc_azolla + float(x[6])
            elif('1164' in tr2tax[x[0]]):
                trichormus = trichormus + 1
                tpm_trichormus = tpm_trichormus + float(x[6])
            there = there + 1

        else:
            not_there = not_there + 1
        #if(not calculated[x[0]]):
            #tr2tax[x[0]]
    
    print("Gesamtzahl an Transkripts in RSEM: ", there + not_there)
    print("Transkripte, die von DIAMOND gefunden wurden :", there)
    print("wurden nicht von DIAMOND gefunden :", not_there)
    print("Transkripte von Nostoc Azolla :", nostoc_azolla)
    print("Transkripte von Trichormus :", trichormus)
    print("Transkripte per Million Nostoc Azolla :", tpm_nostoc_azolla)
    print("Transkripte per Million Trichormus :", tpm_trichormus)


if __name__ == "__main__":
    main()