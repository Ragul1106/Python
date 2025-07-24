import csv
import logging

logging.basicConfig(filename='csv_uploader.log', level=logging.ERROR)

class InvalidCSVFormatError(Exception):
    pass

def upload_csv(filename):
    valid_rows = 0
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                raise InvalidCSVFormatError("Empty CSV file")
                
            for i, row in enumerate(reader, 1):
                try:
                    if not all(field in row for field in ['name', 'age', 'email']):
                        raise InvalidCSVFormatError(f"Missing required fields in row {i}")
                    age = int(row['age'])
                    if age <= 0:
                        raise ValueError(f"Invalid age in row {i}")
                    valid_rows += 1
                except (ValueError, InvalidCSVFormatError) as e:
                    logging.error(f"Row {i} error: {e}")
                    continue
                    
    except FileNotFoundError:
        logging.error("CSV file not found")
        print("Error: File not found")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Error: {e}")
    else:
        print(f"Successfully processed {valid_rows} valid rows")
    finally:
        print("Upload complete")

upload_csv("data.csv")