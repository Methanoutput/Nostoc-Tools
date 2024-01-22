import matplotlib.pyplot as plt

# tpm Nostoc Azolla = 20568.440000000017
# tpm Trichormus = 9563.300000000003
# tpm Eukaryota = 790857.6300000007
# tpm Bacteria = 41208.42999999999

def main():
    isoforms = open("Nostoc-Data/sample_a.isoforms.results", "r") #number 5 is index for tpm
    matches = open("Nostoc-Data/matches_v218_a_taxon", "r")
    tr2tax = {}
    tr2king = {}
    calculated = {}
   
    nostoc_azolla_values = []
    nostoc_azolla_weighted = [0] * 21

    trichormus_values = []
    trichormus_weighted = []
 
    eukaryota_values = []
    eukaryota_weighted = []


    bacteria_values = []
    bacteria_weighted = []
    
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
                nostoc_azolla_values.append(float(x[5]))
            elif('1164' in tr2tax[x[0]]):
                bacteria_values.append(float(x[5]))
                trichormus_values.append(float(x[5]))
            elif('Eukaryota' in tr2king[x[0]]):
                eukaryota_values.append(float(x[5]))
            elif('Bacteria' in tr2king[x[0]]):
                bacteria_values.append(float(x[5]))

    values = [21]
    print(max(nostoc_azolla_values))
    while(max(values) < 421):
        values.append(values[len(values) - 1] + 21)
    print(values)
    print(len(values))

    print(len(nostoc_azolla_values), "länge nostoc azolla values")

    nostoc_azolla_weighted = [sum(1 for value in nostoc_azolla_values if values[i] <= value < values[i+1]) for i in range(len(values)-1)]



    counts = [20568.44, 9563.30, 790857.63, 41208.42]
    print(nostoc_azolla_weighted)
    print(min(nostoc_azolla_values))

    # plt.figure(figsize=(10, 6))
    # Plotting the original counts in blue
    # plt.bar(organisms, counts, color='skyblue', label='TPM')

    # plt.xlabel('Organism')
    # plt.ylabel('Transcript per Million')
    # plt.title('TPM for Different Organisms')
    # plt.xticks(rotation=45)
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.legend()  # Adding a legend to distinguish between the two sets of bars

    # Show the plot
    # plt.show()

if __name__ == "__main__":
    main()