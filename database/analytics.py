"""
analytics.py
------------
Provides workout analytics.
"""

from database.database import get_connection


def workouts_per_exercise():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT exercise, COUNT(*)
        FROM workouts
        GROUP BY exercise
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def calories_over_time():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, calories
        FROM workouts
        ORDER BY date
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def reps_over_time():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, reps
        FROM workouts
        ORDER BY date
    """)

    data = cursor.fetchall()

    conn.close()

    return data