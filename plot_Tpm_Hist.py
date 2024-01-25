import matplotlib.pyplot as plt

# tpm Nostoc Azolla = 20568.440000000017
# tpm Trichormus = 9563.300000000003
# tpm Eukaryota = 790857.6300000007
# tpm Bacteria = 41208.42999999999


def RLperID(rawvalues: list) -> (list,list):
    weighted_values: list = [0] * 20
    if(len(rawvalues) < 1):
        pass
    else:
        step: int = (max(rawvalues) + 1) / 20
        steps: list = [step]
        for i in range(0, 20):
            for j in range(0, len(rawvalues)):
                if(rawvalues[j] > step * i and rawvalues[j] < step * (i + 1)):
                    weighted_values[i] += 1
            if(step*(i + 1) not in steps):
                steps.append(step*(i + 1))
        return weighted_values, steps


def main():
    isoforms = open("/home/jonas/Dokumente/BA-Bioinformatics/kaiju/TaxListMaker/sample_a.isoforms.results", "r") #number 5 is index for tpm
    matches = open("/home/jonas/Dokumente/BA-Bioinformatics/kaiju/TaxListMaker/matches_v218_a_taxon", "r")
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

    testlist : list = []
    for i in range(0, len(trichormus_values)):
        if(trichormus_values[i] < 25):
            testlist.append(trichormus_values[i])
    #trichormus_values.remove(max(trichormus_values))
    nostoc_azolla_weighted, nostoc_azolla_steps = RLperID(nostoc_azolla_values)
    trichormus_weighted, trichormus_steps = RLperID(trichormus_values)
    bacteria_weighted, bacteria_steps = RLperID(bacteria_values)
    eukaryota_weighted, eukaryota_steps = RLperID(eukaryota_values)
    print("----Nostoc Azolla-----")
    print(nostoc_azolla_weighted)
    print(nostoc_azolla_steps)
    print("----------------------")
    print("------Trichormus------")
    print(trichormus_weighted)
    print(trichormus_steps)
    print("----------------------")
    print("--Bacteria--------------")
    print(bacteria_weighted)
    print(bacteria_steps)
    print("-----------------------")
    print("---Eukaryota-------------")
    print(eukaryota_weighted)
    print(eukaryota_steps)
    print("-------------------------")


    plt.figure(figsize=(10, 6))
    #Plotting the original counts in blu
    plt.bar(eukaryota_steps, eukaryota_weighted, color='skyblue', label='TPM', width = 2000.0)

    plt.xlabel('TPM')
    plt.ylabel('Reads')
    plt.title('TPM for Different Organisms')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()  # Adding a legend to distinguish between the two sets of bars

    #Show the plot
    plt.show()

if __name__ == "__main__":
    main()