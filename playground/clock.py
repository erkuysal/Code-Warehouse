import time

# Example usage:
    # get_time = TimeLibraryTime()
    # print("Year:", time_lib_time.get_year())
    # print("Month:", time_lib_time.get_month())
    # print("Day:", time_lib_time.get_day())
    # print("Weekday:", time_lib_time.get_weekday())
    # print("Current timestamp:", time_lib_time.get_timestamp())
    # print("Formatted time:", get_time.format_time())


class TimeLibraryTime:
    def __init__(self):
        self.now = time.localtime()

    def get_year(self):
        return self.now.tm_year

    def get_month(self):
        return self.now.tm_mon

    def get_day(self):
        return self.now.tm_mday

    def get_weekday(self):
        return time.strftime("%A", self.now)

    def get_timestamp(self):
        return time.time()

    def format_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", self.now)


def display_clock():
    try:
        while True:
            # Get the current local time
            current_time = time.localtime()
            # Format the time to display hours, minutes, and seconds
            formatted_time = time.strftime("%H:%M:%S", current_time)
            # Sleep for 1 second
            print(formatted_time)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")


display_clock()

