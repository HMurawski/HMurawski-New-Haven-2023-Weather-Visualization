import csv

filename = "C:\\Users\\USER\Desktop\\python_projects\\New_Haven_2023\\New_Haven_2023_data.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)