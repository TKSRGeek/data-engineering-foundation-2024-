from app.models import User

def main():
    # Example usage:
    # Create a new user
    new_user = User('john_doe', 'john@example.com')
    new_user.save()

    # Fetch all users
    users = User.fetch_all()
    print("All users:")
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
