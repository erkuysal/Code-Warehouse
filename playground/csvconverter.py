import csv


def txt_to_csv(txt_file, csv_file, delimiter=','):
    reminders = []

    # Read the TXT file
    try:
        with open(txt_file, mode='r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(delimiter)
                    if len(parts) == 2:
                        reminders.append({
                            'message': parts[0].strip(),
                            'time': parts[1].strip()
                        })
                    else:
                        print(f"Error: Invalid line format: {line}")
    except FileNotFoundError:
        print(f"Error: File not found - {txt_file}. Please check the file path and name.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Write to the CSV file
    try:
        with open(csv_file, mode='w', newline='') as file:
            fieldnames = ['message', 'time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for reminder in reminders:
                writer.writerow(reminder)
        print(f"Successfully converted {txt_file} to {csv_file}")
    except Exception as e:
        print(f"Error writing the CSV file: {e}")


# Example usage:
txt_file = 'tasks.txt'
csv_file = 'tasks.csv'
txt_to_csv(txt_file, csv_file)