class Request:
    def __init__(self, path, method):
        self.path = path
        self.method = method
        self.processed_by = []


class Middleware:
    def __init__(self):
        self.middlewares = []

    def use(self, middleware):
        self.middlewares.append(middleware)

    def handle_request(self, request, *args, **kwargs):
        for middleware in self.middlewares:
            middleware(request, *args, **kwargs)


def auth_middleware(request, *args, **kwargs):
    print(f"Authenticating request: {request.path}")
    request.processed_by.append('auth')


def log_middleware(request, *args, **kwargs):
    print(f"Logging request: {request.path}")
    request.processed_by.append('log')


# Create middleware pipeline
pipeline = Middleware()
pipeline.use(auth_middleware)
pipeline.use(log_middleware)

# Create a request and process it through the middleware pipeline
req = Request('/home', 'GET')
pipeline.handle_request(req)

print(f"Request processed by: {req.processed_by}")