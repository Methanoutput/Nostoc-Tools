import matplotlib.pyplot as plt

# tpm Nostoc Azolla = 20568.440000000017
# tpm Trichormus = 9563.300000000003
# tpm Eukaryota = 790857.6300000007
# tpm Bacteria = 41208.42999999999

def main():
    values = [21]
    while(max(values) < 421):
        values.append(values[len(values) - 1] + 21)
    print(values)
    counts = [20568.44, 9563.30, 790857.63, 41208.42]

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