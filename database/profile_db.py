"""
profile_db.py
--------------
Handles all user profile database operations.
"""

from database.database import get_connection
from profile.user_profile import UserProfile


def save_user(profile: UserProfile):

    conn = get_connection()
    cursor = conn.cursor()

    # Keep only one profile for now
    cursor.execute("DELETE FROM users")

    cursor.execute(
        """
        INSERT INTO users(
            name,
            age,
            gender,
            height,
            weight,
            goal,
            activity_level
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            profile.name,
            profile.age,
            profile.gender,
            profile.height,
            profile.weight,
            profile.goal,
            profile.activity_level
        )
    )

    conn.commit()
    conn.close()


def load_user():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            age,
            gender,
            height,
            weight,
            goal,
            activity_level
        FROM users
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return UserProfile(
        name=row[0],
        age=row[1],
        gender=row[2],
        height=row[3],
        weight=row[4],
        goal=row[5],
        activity_level=row[6]
    )


def delete_user():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")

    conn.commit()
    conn.close()