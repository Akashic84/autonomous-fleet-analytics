-- currently not used, use in load_data.py to create more accurate database structure and more tables

CREATE TABLE trips (
    trip_id INTEGER PRIMARY KEY,
    vehicle_id TEXT,
    software_version TEXT,
    distance_km REAL,
    duration_min REAL,
    weather TEXT,
    route_type TEXT,
    disengagements INTEGER
);