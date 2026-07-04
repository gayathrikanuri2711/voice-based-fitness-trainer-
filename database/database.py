"""
database.py
------------
Creates the SQLite database and tables.
"""

import sqlite3

DATABASE_NAME = "fitness.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ----------------------------
    # User Profile
    # ----------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        age INTEGER,

        gender TEXT,

        height REAL,

        weight REAL,

        goal TEXT,

        activity_level TEXT
    )
    """)

    # ----------------------------
    # Workout History
    # ----------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        exercise TEXT,

        reps INTEGER,

        duration REAL,

        calories REAL
    )
    """)

    # ----------------------------
    # Achievements
    # ----------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS achievements(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        description TEXT,

        achieved_on TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("Database Created Successfully!")