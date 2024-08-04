import subprocess, csv, sys, time
from datetime import datetime

DOMAINS_PATH = sys.argv[1]
OUTPUT_PATH = 'domain_expiry_info.csv'


def fetch_ssl_expiry_date(domain):
    start_time = time.perf_counter()    # ConVal
    try:
        command = f"curl --insecure -vvI https://{domain} 2>&1 | grep -e 'expire date'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and 'expire date' in result.stdout:
            # Extract date using awk-like logic in Python
            expiry_date = result.stdout.split("expire date:")[1].strip()
            # -------------------------- CONTROL AREA ---------------------------------
            end_time = time.perf_counter()
            print(f"Fetched expiry date for {domain} in {end_time - start_time:.4f} seconds")
            # --------------------------------------------------------------------------
            return expiry_date
        # -------------------------- CONTROL AREA ---------------------------------
        end_time = time.perf_counter()
        print(f"Failed to fetch expiry date for {domain} in {end_time - start_time:.4f} seconds")
        # --------------------------------------------------------------------------
        return None
    except Exception as e:
        # -------------------------- CONTROL AREA ---------------------------------
        end_time = time.perf_counter()
        print(f"Error fetching SSL expiry date for {domain}: {e} in {end_time - start_time:.4f} seconds")
        # --------------------------------------------------------------------------
        return None


def parse_date(date_str):
    # Remove 'GMT' from the date string if it exists
    date_str = date_str.replace(" GMT", "")
    try:
        return datetime.strptime(date_str, "%b %d %H:%M:%S %Y")
    except ValueError:
        return datetime.strptime(date_str, "%b %_d %H:%M:%S %Y")


def format_date(date_str):
    date = parse_date(date_str.strip())
    return date.strftime("%b %d %Y")


def calculate_remaining_time(future_date_str):
    future_date = parse_date(future_date_str.strip())
    current_date = datetime.now()
    remaining_time = future_date - current_date
    return remaining_time


def main():
    domains_file = DOMAINS_PATH
    output_file = OUTPUT_PATH
    data = []

    # Read domains from the file and fetch SSL expiry dates
    with open(domains_file, 'r') as file:
        start_time_loop = time.perf_counter()
        reader = csv.reader(file)
        for line in reader:
            domain = line[0].strip()
            if domain and not domain.startswith('#'):
                expiry_date_str = fetch_ssl_expiry_date(domain)
                if expiry_date_str:
                    remaining_time = calculate_remaining_time(expiry_date_str)
                    formatted_expiry_date = format_date(expiry_date_str)
                    data.append((domain, formatted_expiry_date, remaining_time.days))
        # ----------------------------- CONTROL AREA -------------------------------
        end_time_loop = time.perf_counter()
        print(f"Processing all domains took {end_time_loop - start_time_loop:.4f} seconds")
        # --------------------------------------------------------------------------

    # Sort the data by remaining time in descending order
    sorted_data = sorted(data, key=lambda x: x[2])

    # Write the sorted data to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Domain', 'Expiration Date', 'Remaining (Days)']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for row in sorted_data:
            writer.writerow(row)

        log_date = datetime.now().strftime("%b %d %Y")
        log_time = datetime.now().strftime("%H:%M:%S")
        writer.writerow([' ', ' ', ' '])
        writer.writerow(['- Created At -', log_date, log_time])

    print(f"Data written to {output_file}")

    return sorted_data


if __name__ == "__main__":
    main()
