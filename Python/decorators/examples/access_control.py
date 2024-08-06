def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user['role'] != permission:
                raise PermissionError("You do not have the required permissions")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


@requires_permission('admin')
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


admin_user = {'name': 'Admin', 'role': 'admin'}
normal_user = {'name': 'User', 'role': 'user'}

delete_user(admin_user, 123)
# delete_user(normal_user, 123)  # This will raise a PermissionError