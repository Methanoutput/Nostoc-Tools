#ab : couldnt resolve: 5065, eukaryotic: 814798, bacis: 117741, all: 937604
#a : couldnt resolve: 5119, eukaryotic: 813159, bacis: 123234, all: 941512 

def main():
    f = open("matches_v218_a_taxon", "r")

    bac_count = 0
    euc_count = 0
    all_count = 0
    cant_resolve_sum = 0

    cant_resolve = []

    for x in f:
        x = x.split()
        if (x[13] == "Eukaryota"):
            euc_count += 1
        elif (x[13] == "Bacteria"):
            bac_count += 1
        else:
            cant_resolve_sum += 1
            cant_resolve.append(x)
        all_count += 1


    print(cant_resolve)
    print(cant_resolve_sum)    
    print(euc_count, "\n")
    print(bac_count, "\n")
    print(all_count, "\n")
    
if __name__ == "__main__":
    main()