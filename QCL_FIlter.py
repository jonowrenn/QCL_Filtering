import pandas as pd
import matplotlib.pyplot as plt

# Define thresholds for filtering based on your dataset
thresholds = {
    'efield (kV/cm)': (10, 50),   # Full range of efield
    't_ul (ps)': (0, 25),         # Full range of t_ul
    'z (A)': (-60, 40),           # Expanded range for z
    'g (cm/kA)': (70, 130),       # Expanded range for g
    'fom* (eV ps A^2)': (40, 120),  # Expanded range for fom*
    'Ediff (meV)': (50, 180)      # Expanded range for Ediff
}

# File paths
input_csv_path = '/Users/jonathanwrenn/Desktop/QCL Filtering/filtered_data.csv'
output_csv_path = '/Users/jonathanwrenn/Desktop/QCL Filtering/filtered_results.csv'

# Load the CSV file
df = pd.read_csv(input_csv_path)

# Debug: Print column names and a sample of the dataset
print("Columns in the dataset:", df.columns)
print(df.head())

# Ensure numeric data types for filtering
numeric_columns = list(thresholds.keys())
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing or NaN values
df = df.dropna()

# Apply filters based on thresholds
filtered_df = df[
    (df['efield (kV/cm)'] >= thresholds['efield (kV/cm)'][0]) & (df['efield (kV/cm)'] <= thresholds['efield (kV/cm)'][1]) &
    (df['t_ul (ps)'] >= thresholds['t_ul (ps)'][0]) & (df['t_ul (ps)'] <= thresholds['t_ul (ps)'][1]) &
    (df['z (A)'] >= thresholds['z (A)'][0]) & (df['z (A)'] <= thresholds['z (A)'][1]) &
    (df['g (cm/kA)'] >= thresholds['g (cm/kA)'][0]) & (df['g (cm/kA)'] <= thresholds['g (cm/kA)'][1]) &
    (df['fom* (eV ps A^2)'] >= thresholds['fom* (eV ps A^2)'][0]) & (df['fom* (eV ps A^2)'] <= thresholds['fom* (eV ps A^2)'][1]) &
    (df['Ediff (meV)'] >= thresholds['Ediff (meV)'][0]) & (df['Ediff (meV)'] <= thresholds['Ediff (meV)'][1])
]

# Save the filtered results to a new CSV
filtered_df.to_csv(output_csv_path, index=False)
print(f"Filtered results saved to {output_csv_path}")

# Debug: Number of rows after filtering
print(f"Number of designs after filtering: {len(filtered_df)}")

# Summary statistics for filtered data
if len(filtered_df) > 0:
    print("Summary statistics for filtered results:")
    print(filtered_df.describe())
else:
    print("No rows matched the filtering conditions.")

# Optional: Plot histograms for each metric
def plot_column_histogram(df, column_name, bins=20):
    plt.hist(df[column_name], bins=bins, alpha=0.7, color='blue')
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Plot histograms for each filtered column
for column in numeric_columns:
    if column in filtered_df.columns and not filtered_df.empty:
        plot_column_histogram(filtered_df, column)
