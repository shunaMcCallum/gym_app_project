PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS workouts;

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR,
    last_name VARCHAR,
    dob DATE,
    active BOOLEAN
);

CREATE TABLE workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    date DATE,
    description TEXT,
    duration INTEGER,
    capacity INTEGER,
    capacity_filled INTEGER,
    active BOOLEAN
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    workout_id INTEGER NOT NULL,
        FOREIGN KEY (member_id)
            REFERENCES members(id) ON DELETE CASCADE,
        FOREIGN KEY (workout_id)
            REFERENCES workouts(id) ON DELETE CASCADE
);