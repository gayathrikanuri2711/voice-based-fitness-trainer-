"""
workout_db.py
-------------
Handles workout history operations.
"""

from database.database import get_connection


def save_workout(date, exercise, reps, duration, calories):
    """
    Save a completed workout.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO workouts(
            date,
            exercise,
            reps,
            duration,
            calories
        )
        VALUES (?,?,?,?,?)
        """,
        (
            date,
            exercise,
            reps,
            duration,
            calories
        )
    )

    conn.commit()
    conn.close()


def get_all_workouts():
    """
    Returns all workouts.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM workouts
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_total_workouts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM workouts
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_reps():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(reps)
        FROM workouts
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result if result else 0


def get_total_calories():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(calories)
        FROM workouts
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return round(result, 2) if result else 0


def clear_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM workouts")

    conn.commit()
    conn.close()