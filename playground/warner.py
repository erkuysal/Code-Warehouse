import time


class ClockWithReminder:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, reminder_time, message):
        self.reminders.append((reminder_time, message))
        print(f"Reminder set for {reminder_time}: {message}")

    def check_reminders(self, current_time):
        formatted_time = time.strftime("%H:%M:%S", current_time)
        for reminder_time, message in self.reminders:
            if formatted_time == reminder_time:
                print(f"\nReminder! {formatted_time}: {message}")
                self.reminders.remove((reminder_time, message))

    def display_clock(self):
        try:
            while True:
                # Get the current local time
                current_time = time.localtime()
                # Format the time to display hours, minutes, and seconds
                formatted_time = time.strftime("%H:%M:%S", current_time)
                # Print the formatted time
                print(formatted_time)
                # Check for reminders
                self.check_reminders(current_time)
                # Sleep for 1 second
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nClock stopped.")


# Create a clock instance
clock = ClockWithReminder()

# Set some reminders (format "HH:MM:SS")
clock.set_reminder("10:36:00", "Meeting with team.")
clock.set_reminder("10:37:00", "Call with client.")

# Run the clock
clock.display_clock()