import os
import csv

from dotenv import load_dotenv

# Load .env file into environment
load_dotenv()

# Get environment variables
DAT_DIRECTORY = os.getenv('DAT_DIRECTORY', "data")
CSV_FILENAME = os.getenv('CSV_FILENAME', "temperature_log.csv")
FILE_EXTENSION = os.getenv('FILE_EXTENSION', ".dat")
TEMP_PREFIX = os.getenv('TEMP_PREFIX', "TEMP")

def extract_temperature_from_line(line):
    if line.startswith(TEMP_PREFIX):
        temp_values = line.split()[1:]
        if len(temp_values) >= 1:
            return temp_values[0]
    return None

def process_dat_file(filepath):
    with open(filepath, "r") as dat_file:
        for line in dat_file:
            temp = extract_temperature_from_line(line)
            if temp:
                return os.path.basename(filepath), temp
    return None

def write_to_csv(rows):
    with open(CSV_FILENAME, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(["Filename", "Temperature"])
        for row in rows:
            csv_writer.writerow(row)

if __name__ == "__main__":
    try:
        # Filter only .dat files
        dat_files = [f for f in os.listdir(DAT_DIRECTORY) if f.endswith(FILE_EXTENSION)]
        rows_to_write = []

        for filename in dat_files:
            filepath = os.path.join(DAT_DIRECTORY, filename)
            row = process_dat_file(filepath)
            if row:
                rows_to_write.append(row)
        
        write_to_csv(rows_to_write)
        print("Temperature extraction complete. Check temperature_log.csv")

    except Exception as e:
        print(f"An error occurred: {e}")
