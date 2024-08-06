import argparse


def create_user(username, password, **kwargs):
    email = kwargs.get('email', 'N/A')
    role = kwargs.get('role', 'user')
    print(f"Creating user: {username}, Password: {password}, Email: {email}, Role: {role}")


def delete_user(username, **kwargs):
    force = kwargs.get('force', False)
    print(f"Deleting user: {username}, Force: {force}")


def list_users(*args, **kwargs):
    filter_by_role = kwargs.get('role')
    print(f"Listing users, Filter by role: {filter_by_role}")
    for user in args:
        print(f"User: {user}")


def main():
    parser = argparse.ArgumentParser(description="User management CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Create user command
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('username')
    create_parser.add_argument('password')
    create_parser.add_argument('--email')
    create_parser.add_argument('--role')

    # Delete user command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('username')
    delete_parser.add_argument('--force', action='store_true')

    # List users command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('users', nargs='*')
    list_parser.add_argument('--role')

    args = parser.parse_args()

    if args.command == 'create':
        create_user(args.username, args.password, email=args.email, role=args.role)
    elif args.command == 'delete':
        delete_user(args.username, force=args.force)
    elif args.command == 'list':
        list_users(*args.users, role=args.role)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()