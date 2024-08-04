import csv
import subprocess
import pandas as pd
from datetime import datetime


DOMAINS_PATH = 'domain_SSL/SSL_domainler.txt'


def fetch_ssl_expiry_date(domain):
    try:
        command = f"curl --insecure -vvI https://{domain} 2>&1 | grep -e 'expire date'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and 'expire date' in result.stdout:
            # Extract date using awk-like logic in Python
            expiry_date = result.stdout.split("expire date:")[1].strip()
            return expiry_date
        return None
    except Exception as e:
        print(f"Error fetching SSL expiry date for {domain}: {e}")
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
    domains_file = DOMAINS_PATH  # File containing the list of domains
    data = []

    # Read domains from the file and fetch SSL expiry dates
    with open(domains_file, 'r') as file:
        for line in file:
            domain = line.strip()
            if domain and not domain.startswith('#'):
                expiry_date_str = fetch_ssl_expiry_date(domain)
                # ms
                if expiry_date_str:
                    remaining_time = calculate_remaining_time(expiry_date_str)
                    data.append((domain, expiry_date_str, remaining_time))
                    #ms
        #ms

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['domain', 'expiry_date', 'remaining_time'])

    # Sort the DataFrame by remaining time in ascending order
    df = df.sort_values(by='remaining_time')  # add ascending=False as parameter to change.

    # Print the sorted data
    for index, row in df.iterrows():
        domain = row['domain']
        expiry_date = row['expiry_date']
        remaining_time = row['remaining_time']

        # Format the remaining time nicely
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Domain: {domain} Kalan Sure: {days}")
        # print(f"Expiry date: {expiry_date}")
        # print(f"Remaining time: {days} days left\n")


if __name__ == "__main__":
    main()
