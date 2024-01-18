import numpy as np
#TODO: Also der Anzahl die auch im Genom sein sollte. Das wäre ja schon mal gut. Da wir ja eine representative Genanzahl bekommen
#zusätzlich entspricht das dann ja auch noch in etwa 50% der bakteriellen Sequenzen was Nostoc azollae zugeordnet wird
#jetzt habe ich hier noch fragen: was ist die TPM Verteilung. Sind nur einige viel und viele wenig exprimiert?
#Also sowohl bei den Eukaryoten als auch Baktis und Nostoc azollae im spezifischen.
#Hier könntest du einmal alle TPM rausziehen die zur jeweiligen Kategorie gehören und (a) Mittelwert ± Standardabweichung ausrechnen und (b) alle TPM einer Kategorie (Kategorien: Euk, Bakt, Trichormus, Nostoc azollae) als histogramm (eins pro Kategorie) darstellen
# Plots 
# Schreiben

def main():
    isoforms = open("Nostoc-Data/sample_a.isoforms.results", "r") #number 5 is index for tpm
    matches = open("Nostoc-Data/matches_v218_a_taxon", "r")
    tr2tax = {}
    tr2king = {}
    calculated = {}

    not_there = 0
    there = 0

    nostoc_azolla = 0
    nostoc_azolla_values = []
    tpm_nostoc_azolla = 0

    trichormus = 0
    trichormus_values = []
    tpm_trichormus = 0

    eukaryota = 0
    eukaryota_values = []
    tpm_eukorayota = 0

    bacteria = 0
    bacteria_values = []
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
                nostoc_azolla = nostoc_azolla + 1 #how many nostoc transcript
                bacteria = bacteria + 1 #how many bacteria transcripts

                tpm_bacteria = tpm_bacteria + float(x[5]) #tpm value for sum
                tpm_nostoc_azolla = tpm_nostoc_azolla + float(x[5]) #tpm value for sum

                bacteria_values.append(float(x[5]))
                nostoc_azolla_values.append(float(x[5]))
            elif('1164' in tr2tax[x[0]]):
                trichormus = trichormus + 1
                bacteria = bacteria + 1
                tpm_trichormus = tpm_trichormus + float(x[5])
                bacteria_values.append(float(x[5]))
                tpm_bacteria = tpm_bacteria + float(x[5])
                trichormus_values.append(float(x[5]))
            elif('Eukaryota' in tr2king[x[0]]):
                eukaryota = eukaryota + 1
                tpm_eukorayota = tpm_eukorayota + float(x[5])
                eukaryota_values.append(float(x[5]))
            elif('Bacteria' in tr2king[x[0]]):
                bacteria = bacteria + 1
                tpm_bacteria = tpm_bacteria + float(x[5]) 
                bacteria_values.append(float(x[5]))
            there = there + 1

        else:
            not_there = not_there + 1
        #if(not calculated[x[0]]):
            #tr2tax[x[0]]
    print("-------------------------")
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
    print("-------------------------")
    print("Mittelwert Nostoc Azolla :", tpm_nostoc_azolla / nostoc_azolla)
    print("Mittelwert Trichormus :", tpm_trichormus / trichormus)
    print("Mittelwert Eukaryota :", tpm_eukorayota / eukaryota)
    print("Mittelwert Bacteria :", tpm_bacteria / bacteria)
    print("-------------------------")
    print("Standardabweichung Nostoc Azolla :", np.std(nostoc_azolla_values))
    print("Standardabweichung Trichormus :", np.std(trichormus_values))
    print("Standardabweichung Bakterien :", np.std(bacteria_values))
    print("Standardabweichung Eukaryoten :", np.std(eukaryota_values))
    print("-------------------------")
    print("Mittelwert Nostoc Azolla ± Standardabweichung :", (tpm_nostoc_azolla / nostoc_azolla) +  np.std(nostoc_azolla_values), "bis", (tpm_nostoc_azolla / nostoc_azolla) - np.std(nostoc_azolla_values))  
    print("Mittelwert Trichormus ± Standardabweichung :", (tpm_trichormus / trichormus) + np.std(trichormus_values), "bis", (tpm_trichormus / trichormus) - np.std(trichormus_values))
    print("Mittelwert Bakterien ± Standardabweichung :", (tpm_bacteria / bacteria) + np.std(bacteria_values), "bis", (tpm_bacteria / bacteria) - np.std(bacteria_values))
    print("Mittelwert Eukaryoten ± Standardabweichung :", (tpm_eukorayota / eukaryota) + np.std(eukaryota_values), "bis", (tpm_eukorayota / eukaryota) - np.std(eukaryota_values))

if __name__ == "__main__":
    main()