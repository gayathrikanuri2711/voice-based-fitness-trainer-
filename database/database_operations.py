from database.database import get_connection


# ----------------------------
# User Operations
# ----------------------------

def add_user(name, age, gender, height, weight, goal, activity_level):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users
        (name, age, gender, height, weight, goal, activity_level)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, height, weight, goal, activity_level))

    conn.commit()
    conn.close()


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return users


def update_weight(user_id, weight):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET weight=? WHERE id=?",
        (weight, user_id)
    )

    conn.commit()
    conn.close()


# ----------------------------
# Workout Operations
# ----------------------------

def add_workout(date, exercise, reps, duration, calories):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO workouts
        (date, exercise, reps, duration, calories)
        VALUES (?, ?, ?, ?, ?)
    """, (date, exercise, reps, duration, calories))

    conn.commit()
    conn.close()


def get_workouts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()

    conn.close()

    return workouts


def delete_workout(workout_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM workouts WHERE id=?",
        (workout_id,)
    )

    conn.commit()
    conn.close()