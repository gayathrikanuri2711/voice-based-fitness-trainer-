from profile.user_profile import UserProfile

from database.profile_db import (
    save_user,
    load_user,
    delete_user
)

user = UserProfile(
    name="Gayathri",
    age=20,
    gender="Female",
    height=165,
    weight=60,
    goal="Fitness",
    activity_level="Moderate"
)

print("Saving user...")
save_user(user)

print("\nLoading user...")
loaded = load_user()

print(loaded)

print("\nDeleting user...")
delete_user()

print("\nLoading again...")
print(load_user())