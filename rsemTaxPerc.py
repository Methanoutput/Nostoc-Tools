def main():
    isoforms = open("sample_a.isoforms.results", "r") #number 6 is index for tpm
    matches = open("matches_v218_a_taxon", "r")
    tr2tax = {}
    calculated = {}
    nostoc_azolla = 0
    
    for x in matches:
        x = x.split()
        tr2tax[x[0]] = x[12]
        calculated[x[0]] = False
    for x in isoforms:
        x = x.split()
        if(not calculated[x[0]]):
            tr2tax[x[0]]


if __name__ == "__main__":
    main()