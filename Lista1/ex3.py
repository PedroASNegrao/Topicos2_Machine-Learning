import os
import pandas as pd
import matplotlib.pyplot as plt

# Set your path to the folder containing the .csv files
PATH = './Data/' # Use your path

# Fetch all files in path
fileNames = os.listdir(PATH)

# Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

IPCA = pd.DataFrame(pd.read_csv(PATH + fileNames[0]))
Desemprego = pd.DataFrame(pd.read_csv(PATH + fileNames[1]))

Desemprego = Desemprego.set_index("Data")
IPCA = IPCA.set_index("Data")

print(Desemprego.head())
print(IPCA.head())

df3 = pd.merge(IPCA, Desemprego, left_index=True, right_index=True)
df3 = df3[[' IPCA ','Taxa de desemprego ']]
print(df3.head())

plt.plot(df3.iloc[:, 0], label="IPCA")
plt.plot(df3.iloc[:, 1], label="Tx. Desemprego")
#plt.plot(df3)

#print(df3.iloc[:, 0])
plt.legend()
plt.show()

#Desemprego.iloc[0,0]
"""
# Loop over all files
for file in fileNames:

    # Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col = 0)

    # Create line for every file
    plt.plot(df)

# Generate the plot
plt.show()
"""