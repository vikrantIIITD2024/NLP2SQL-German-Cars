import sqlite3

DB = "car_specs_database.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

print("Optimizing database...\n")

# Enable Foreign Keys
cursor.execute("PRAGMA foreign_keys = ON;")

# WAL Mode (better performance)
cursor.execute("PRAGMA journal_mode = WAL;")

# Better cache
cursor.execute("PRAGMA cache_size = 10000;")

# Better query planner
cursor.execute("PRAGMA optimize;")

# -----------------------------
# Indexes
# -----------------------------

indexes = [

"""
CREATE INDEX IF NOT EXISTS idx_brand
ON master_overview(brand);
""",

"""
CREATE INDEX IF NOT EXISTS idx_model
ON master_overview(model);
""",

"""
CREATE INDEX IF NOT EXISTS idx_segment
ON master_overview(segment);
""",

"""
CREATE INDEX IF NOT EXISTS idx_launch_year
ON master_overview(launch_year);
""",

"""
CREATE INDEX IF NOT EXISTS idx_body_type
ON master_overview(body_type);
""",

"""
CREATE INDEX IF NOT EXISTS idx_engine_car
ON engine_configuration(car_id);
""",

"""
CREATE INDEX IF NOT EXISTS idx_power_car
ON power_performance(car_id);
""",

"""
CREATE INDEX IF NOT EXISTS idx_price_car
ON price(car_id);
""",

"""
CREATE INDEX IF NOT EXISTS idx_safety_car
ON safety(car_id);
""",

"""
CREATE INDEX IF NOT EXISTS idx_dimension_car
ON dimensions(car_id);
""",

"""
CREATE INDEX IF NOT EXISTS idx_rating_car
ON ratings_reviews(car_id);
"""

]

for sql in indexes:
    cursor.execute(sql)

conn.commit()

print("Optimization complete!")

conn.close()