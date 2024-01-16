def main():
    isoforms = open("Nostoc-Data/sample_ab.isoforms.results", "r") #number 6 is index for tpm
    matches = open("Nostoc-Data/matches_v218_taxon", "r")
    tr2tax = {}
    tr2king = {}
    calculated = {}

    not_there = 0
    there = 0

    nostoc_azolla = 0
    trichormus = 0

    tpm_nostoc_azolla = 0
    tpm_trichormus = 0

    eukaryota = 0
    tpm_eukorayota = 0

    bacteria = 0
    tpm_bacteria = 0
    
    for x in matches:
        x = x.split()
        if(x[0] not in tr2tax):
            tr2tax[x[0]] = x[12]
        else:
            tr2tax[x[0]] = tr2tax[x[0]] + x[12]
        calculated[x[0]] = False
        if(x[0] not in tr2king):
            tr2king[x[0]] = x[13]
    for x in isoforms:
        x = x.split()
        if(x[0] in calculated):
            if('551115' in tr2tax[x[0]]):
                nostoc_azolla = nostoc_azolla + 1
                bacteria = bacteria + 1
                print(x[0])
                print(tr2tax[x[0]])
                tpm_bacteria = tpm_bacteria + float(x[5])
                tpm_nostoc_azolla = tpm_nostoc_azolla + float(x[5])
            elif('1164' in tr2tax[x[0]]):
                trichormus = trichormus + 1
                bacteria = bacteria + 1
                tpm_trichormus = tpm_trichormus + float(x[5])
                tpm_bacteria = tpm_bacteria + float(x[5])
            elif('Eukaryota' in tr2king[x[0]]):
                eukaryota = eukaryota + 1
                tpm_eukorayota = tpm_eukorayota + float(x[5])
            elif('Bacteria' in tr2king[x[0]]):
                bacteria = bacteria + 1
                tpm_bacteria = tpm_bacteria + float(x[5]) 
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
    print("-------------------------")
    print("Transkripte von Eukaryota :", eukaryota)
    print("Transkripte per Million Eukaryota :", tpm_eukorayota)
    print("Transkripte von Bacteria :", bacteria)
    print("Transkripte per Million Bacteria :", tpm_bacteria)


if __name__ == "__main__":
    main()