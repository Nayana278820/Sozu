import csv
import math

def read_psd_data(filename):
    psd_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            psd_data.append([float(val) for val in row])
    return psd_data

def compute_log_values(psd_data):
    log_data = []
    for row in psd_data:
        log_row = [math.log10(value) for value in row]
        log_data.append(log_row)
    return log_data

def write_log_data(log_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(log_data)

def main():
    input_filename = 'psdFreq_changes_newCircuit1.csv'
    output_filename = 'log_newCircuit1.csv'

    psd_data = read_psd_data(input_filename)
    log_data = compute_log_values(psd_data)
    write_log_data(log_data, output_filename)

if __name__ == "__main__":
    main()
