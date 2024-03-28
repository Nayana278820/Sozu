import csv
import matplotlib.pyplot as plt
import numpy as np

# Function to read PSD values from CSV file
def read_psd_values(filename):
    psd_values = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the first row (empty row)
        next(reader)
        # Read PSD values
        for row in reader:
            if row:
                # Convert strings to floats and handle significant figure format
                psd_values.append([float(value.split('E')[0]) if value else 0.0 for value in row])
    return psd_values

# Function to create plot
def plot_psd_changes(psd_values):
    num_columns = len(psd_values[0])
    
    # Plot each column separately
    plt.figure(figsize=(10, 6))
    for col in range(num_columns):
        x_values = []
        y_values = []
        for i in range(len(psd_values) - 1):
            diff = psd_values[i + 1, col] - psd_values[i, col]
            # Check if the difference is a whole number
            if abs(diff - round(diff)) < 1e-6:
                x_values.append(i)
                y_values.append(psd_values[i, col])
        plt.plot(x_values, y_values, 'o-', label=f'Index {col}')
    plt.xlabel('Row Index')
    plt.ylabel('PSD Value')
    plt.title('PSD Value Changes from Row to Row')
    plt.legend()  # Specify legend location
    plt.show()


# Main function
def main():
    # Specify the filename
    filename = 'NEW_psd_changes.csv'
    
    # Read PSD values from CSV file
    psd_values = read_psd_values(filename)
    
    # Create plot to show PSD value changes row by row for each index
    plot_psd_changes(np.array(psd_values))

if __name__ == '__main__':
    main()

# # Function to create plot
# def plot_psd_differences(psd_values):
#     # Calculate differences between consecutive rows
#     differences = np.diff(psd_values, axis=0)
#     print(differences)
    
#     # Plot differences
#     plt.figure(figsize=(10, 6))
#     plt.imshow(differences, aspect='auto', cmap='coolwarm')
#     plt.colorbar(label='Difference in PSD Values')
#     plt.xlabel('Frequency Index')
#     plt.ylabel('Scan Number Difference')
#     plt.title('Differences in PSD Values Between Consecutive Scans')
#     plt.show()

# # Main function
# def main():
#     # Specify the filename
#     filename = 'NEW_psd_changes.csv'
    
#     # Read PSD values from CSV file
#     psd_values = read_psd_values(filename)
    
#     # Create plot to show differences in PSD values
#     plot_psd_differences(psd_values)

# if __name__ == '__main__':
#     main()

