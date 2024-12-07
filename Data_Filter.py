import pandas as pd

# Load the CSV file
file_path = '/Users/jonathanwrenn/Desktop/QCL Filtering/QCL-layer_10-4rep-rand-m2A_3A-efield_0-10-150-v22-dataset.csv'
df = pd.read_csv(file_path)

# Display the column names
print("Columns in the CSV file:", df.columns)

# Select only the columns you need
selected_columns = ['efield (kV/cm)', 't_ul (ps)', 'z (A)', 'g (cm/kA)', 'fom* (eV ps A^2)', 'Ediff (meV)']  # Replace with actual column names
filtered_df = df[selected_columns]

# Display the filtered data
print("Filtered Data:")
print(filtered_df.head())

# Perform analysis on the filtered data
print("Summary Statistics:")
print(filtered_df.describe())

# Save the filtered data to a new CSV file (optional)
output_file = '/Users/jonathanwrenn/Desktop/QCL Filtering'
filtered_df.to_csv('filtered_data.csv', index=False)
print("Filtered data saved to 'filtered_data.csv'")
