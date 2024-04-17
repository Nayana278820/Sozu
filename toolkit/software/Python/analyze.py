import csv

# Function to read the PSD data from the CSV file
def read_psd_data(filename):
    psd_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            psd_data.append([float(val) for val in row])
    return psd_data



# Record all the values exceeding the threshold for every 20 values in the row. 
# Store the highest difference that is exceeding the threshold in those 20 values and store 
# it in the exceeding_values array. Then move on to the next 20 values in the row, do the same thing. 
# Look at all the values exceeding the threshold in those 20 values and store the one with the highest 
#difference.

def compare_psd(psd_data, freq_range, threshold=11):
    prev_psd_scan = psd_data[0]  # First row as the previous PSD scan
    count = 0  # Counter to keep track of differences exceeding threshold
    for i in range(1, len(psd_data)):
        exceeding_values = []  # Array to store PSD values exceeding the threshold in each row
        for j in range(0, len(psd_data[i]), 20):
            max_diff = 0
            max_bin = None
            for k in range(j, min(j+20, len(psd_data[i]))):
                if (psd_data[i][k] - prev_psd_scan[k]) > threshold:
                    diff = (psd_data[i][k] - prev_psd_scan[k])
                    if diff > max_diff:
                        max_diff = diff
                        max_bin = k
            if max_bin is not None:
                exceeding_values.append((max_bin, psd_data[i][max_bin]))  # Store the bin number and PSD value
                count += 1  # Increment count for each difference exceeding threshold
                print(f"Frequency: {freq_range[max_bin]} MHz, PSD Value: {psd_data[i][max_bin]}, PSD Difference: {max_diff}")
        prev_psd_scan = psd_data[i]  # Update previous PSD scan
    print("Total differences exceeding threshold:", count)



# Put each value that crosses the threshold that is in the same 
# row in an array. Only print the highest value in that array. 
# That way, each row, only has one psd_value peak

# def compare_psd(psd_data, freq_range, threshold=2.80):
#     # old circuit threshold - 2.8
#     count = 0  # Counter to keep track of differences exceeding threshold
#     prev_psd_scan = psd_data[0]  # Initialize previous PSD scan
#     for i in range(1, len(psd_data)):
#         exceeding_values = []  # Array to store PSD values exceeding the threshold in each row
#         for j in range(len(psd_data[i])):
#             if psd_data[i][j] - psd_data[i-1][j] > threshold:
#                 exceeding_values.append((j, psd_data[i][j]))  # Store the bin number and PSD value
#         if exceeding_values:  # Check if there are exceeding values in the row
#             max_value = max(exceeding_values, key=lambda x: x[1])  # Find the maximum PSD value
#             bin_number, max_psd_value = max_value
#             psd_difference = max_psd_value - prev_psd_scan[bin_number]  # Calculate PSD difference
#             count += 1
#             print(f"Row: {i}, Bin: {bin_number}, Frequency: {freq_range[bin_number]} MHz, PSD Value: {max_psd_value}, PSD Difference: {psd_difference}")
#             # Update previous PSD scan
#             prev_psd_scan = psd_data[i]  # Update previous PSD scan for the next iteration
#     print("Total differences exceeding threshold:", count)

# Myabe skip 20 values after finding an exceeding value, that way you leave some gap between each frequency change
# but can also capture multiple frequency chnages in that row
# def compare_psd(psd_data, freq_range, threshold=2.80):
#     # old circuit threshold - 2.8
#     count = 0  # Counter to keep track of differences exceeding threshold
#     prev_psd_scan = psd_data[0]  # Initialize previous PSD scan
#     i = 1  # Initialize row index
#     while i < len(psd_data):
#         exceeding_values = []  # Array to store PSD values exceeding the threshold in each row
#         j = 0  # Initialize bin index
#         while j < len(psd_data[i]):
#             if psd_data[i][j] - psd_data[i-1][j] > threshold:
#                 exceeding_values.append((j, psd_data[i][j]))  # Store the bin number and PSD value
#                 bin_number = j
#                 max_psd_value = psd_data[i][j]
#                 psd_difference = max_psd_value - prev_psd_scan[bin_number]  # Calculate PSD difference
#                 count += 1
#                 print(f"Row: {i}, Bin: {bin_number}, Frequency: {freq_range[bin_number]} MHz, PSD Value: {max_psd_value}, PSD Difference: {psd_difference}")
#                 # Skip the next 20 values
#                 j += 20
#             else:
#                 j += 1
#         # Update previous PSD scan
#         prev_psd_scan = psd_data[i]  # Update previous PSD scan for the next iteration
#         i += 1  # Move to the next row
#     print("Total differences exceeding threshold:", count)


def main():
    filename = 'psdFreq_changes_newCircuit2.csv'  # Update with your CSV file name
    psd_data = read_psd_data(filename)
    
    # Assuming you have freq_range available from your Waterfall class
    freq_start = 555e6 - 2.4e6 / 2
    freq_step = 2.4e6 / (1024 * 4)
    freq_range = [freq_start + i * freq_step for i in range(len(psd_data[0]))]

    compare_psd(psd_data, freq_range)

if __name__ == "__main__":
    main()
