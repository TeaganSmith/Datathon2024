import csv

def read_data_from_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Clean and split the line by tab (\t)
            line_data = line.strip().split('\t')
            if len(line_data) == 7:  # Ensuring all required fields are present
                data.append(line_data)
    return data

def write_data_to_csv(data, output_file):
    headers = ['Date', 'Town', 'State/Province', 'Latitude', 'Longitude', 'Number', 'Image']
    
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write headers
        csv_writer.writerow(headers)
        # Write the data
        for row in data:
            csv_writer.writerow(row)

def main():
    input_txt_file = 'data.txt'  # Path to your input txt file
    output_csv_file = 'adult_monarch_sightings.csv'  # Path to the output CSV file
    
    # Step 1: Read data from txt file
    data = read_data_from_txt(input_txt_file)
    
    # Step 2: Write data to CSV
    write_data_to_csv(data, output_csv_file)
    print(f"Data has been successfully written to {output_csv_file}")

if __name__ == "__main__":
    main()