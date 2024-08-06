class EventSystem:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, event_name, handler):
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    def trigger_event(self, event_name, *args, **kwargs):
        if event_name in self.handlers:
            for handler in self.handlers[event_name]:
                handler(*args, **kwargs)


# Define some event handlers
def on_user_registered(user_name, email):
    print(f"User registered: {user_name} with email {email}")


def on_user_logged_in(user_name, **kwargs):
    timestamp = kwargs.get('timestamp')
    print(f"User logged in: {user_name} at {timestamp}")


# Create an event system and register handlers
event_system = EventSystem()
event_system.register_handler('user_registered', on_user_registered)
event_system.register_handler('user_logged_in', on_user_logged_in)

# Trigger events
event_system.trigger_event('user_registered', 'Alice', 'alice@example.com')
event_system.trigger_event('user_logged_in', 'Alice', timestamp='2024-08-06 10:00:00')