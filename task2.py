import csv
import os

print("hello world")

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./Task2.csv"

# write result to csv file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # add a csv header
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # read data csv file
    for file in os.listdir(DATA_DIRECTORY):
        with open(f'{DATA_DIRECTORY}/{file}', "r") as current_reading_csv:
            reader = csv.reader(current_reading_csv)
            for record in reader:
                product = record[0]
                print(record)
                # write record in output csv if product name is pink morsel
                if product == "pink morsel":
                    price = float(record[1][1:])
                    quantity = int(record[2])
                    date = record[3]
                    region = record[4]
                    sales = price * quantity

                    output_row = [sales, date, region]
                    writer.writerow(output_row)