import matplotlib.pyplot as plt

# tpm Nostoc Azolla = 20568.440000000017
# tpm Trichormus = 9563.300000000003
# tpm Eukaryota = 790857.6300000007
# tpm Bacteria = 41208.42999999999


def RLperID(rawvalues: list) -> list:
    weighted_values: list = [0] * 20
    if(len(rawvalues) < 1):
        pass
    else:
        step: int = (max(rawvalues) + 1) / 20
        for i in range(0, 20):
            for j in range(0, len(rawvalues)):
                if(rawvalues[j] > step * i and rawvalues[j] < step * (i + 1)):
                    weighted_values[i] += 1
        return weighted_values


def main():
    isoforms = open("Nostoc-Data/sample_a.isoforms.results", "r") #number 5 is index for tpm
    matches = open("Nostoc-Data/matches_v218_a_taxon", "r")
    tr2tax = {}
    tr2king = {}
    calculated = {}
   
    nostoc_azolla_values = []
    nostoc_azolla_weighted = [0] * 21

    trichormus_values = []
    trichormus_weighted = [0] * 21

    eukaryota_values = []
    eukaryota_weighted = [0] * 21


    bacteria_values = []
    bacteria_weighted = [0] * 21
    
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
                bacteria_values.append(float(x[5]))
                if(float(x[5]) > 0.9):
                    nostoc_azolla_values.append(float(x[5]))
            elif('1164' in tr2tax[x[0]]):
                bacteria_values.append(float(x[5]))
                trichormus_values.append(float(x[5]))
            elif('Eukaryota' in tr2king[x[0]]):
                eukaryota_values.append(float(x[5])) 
            elif('Bacteria' in tr2king[x[0]]):
                bacteria_values.append(float(x[5]))

    nostoc_azolla_weighted = RLperID(nostoc_azolla_values)
    trichormus_weighted = RLperID(trichormus_values)
    print(testlist)
    print(testlist_2)
    print(sum(testlist))
    print(len(nostoc_azolla_values))
    return




    #values = [500]
    #print(max(nostoc_azolla_values))
    #while(max(values) < 10000):
        #values.append(values[len(values) - 1] + 500)
    #print(values)
    #print(len(values))

    #print(len(nostoc_azolla_values), "länge nostoc azolla values")
    #nostoc_azolla_weighted = [sum(1 for value in nostoc_azolla_values if values[i] <= value < values[i+1]) for i in range(len(values)-1)]
    #print(nostoc_azolla_values)
    #count = 0
    #for i in range(0, len(nostoc_azolla_values)):
        #if(nostoc_azolla_values[i] > 21 and nostoc_azolla_values[i] < 42):
            #count += 1
    #print(count)
    #bacteria_weighted = [sum(1 for value in bacteria_values if values[i] <= value < values[i+1]) for i in range(len(values)-1)]


    print("bacteria", len(bacteria_values))
    print("bacteria max",max(bacteria_values))
    print("trichormus",len(trichormus_values)) 
    print("trichormus max",max(trichormus_values))
    print("eukaryota ",len(eukaryota_values)) 
    print("eukaryota max",max(eukaryota_values))


    #print(bacteria_weighted)
    #print(bacteria_values)

    #counts = [20568.44, 9563.30, 790857.63, 41208.42]
    #print(nostoc_azolla_weighted, len(nostoc_azolla_weighted))
    #nostoc_azolla_weighted_tmp = [76, 26, 11, 6, 2, 1, 6, 0, 2, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    #print(values, len(values))

    #plt.figure(figsize=(10, 6))
    #Plotting the original counts in blue
    #plt.bar(values, nostoc_azolla_weighted_tmp, color='skyblue', label='TPM')

    #plt.xlabel('TPM')
    #plt.ylabel('Reads')
    #plt.title('TPM for Different Organisms')
    #plt.xticks(rotation=45)
    #plt.grid(axis='y', linestyle='--', alpha=0.7)
    #plt.legend()  # Adding a legend to distinguish between the two sets of bars

    #Show the plot
    #plt.show()

if __name__ == "__main__":
    main()