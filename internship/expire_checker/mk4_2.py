import csv
import subprocess
import pandas as pd
from datetime import datetime
import time


DOMAINS_PATH = 'domain_SSL/SSL_domainler.txt'


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


def calculate_remaining_time(future_date_str):
    future_date = parse_date(future_date_str.strip())
    current_date = datetime.now()
    remaining_time = future_date - current_date
    return remaining_time


def main():
    start_time_main = time.perf_counter()  # ConVal

    domains_file = DOMAINS_PATH
    data = {}

    # Read domains from the file and fetch SSL expiry dates
    with open(domains_file, 'r') as file:
        start_time_loop = time.perf_counter()  # ConVal
        for line in file:
            domain = line.strip()
            if domain and not domain.startswith('#'):
                expiry_date_str = fetch_ssl_expiry_date(domain)
                if expiry_date_str:
                    remaining_time = calculate_remaining_time(expiry_date_str)
                    data[domain] = (expiry_date_str, remaining_time)
                    print(f"Stored data for {domain}: {data[domain]}")
        # ----------------------------- CONTROL AREA -------------------------------
        end_time_loop = time.perf_counter()
        print(f"Processing all domains took {end_time_loop - start_time_loop:.4f} seconds")
        # --------------------------------------------------------------------------

    sorted_data = sorted(data.items(), key=lambda x: x[1][1])

    start_time_print = time.perf_counter()  # ConVal
    for domain, (expiry_date, remaining_time) in sorted_data:
        days = remaining_time.days
        print(f"Domain: {domain} // Expiry date: {expiry_date} // Expiration In > {days} days <")
    # ----------------------------- CONTROL AREA -------------------------------
    end_time_main = time.perf_counter()
    print(f"Total execution time: {end_time_main - start_time_main:.4f} seconds")
    # --------------------------------------------------------------------------


if __name__ == "__main__":
    main()
