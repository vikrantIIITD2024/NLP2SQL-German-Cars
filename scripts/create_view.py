import sqlite3

DB_FILE = "car_specs_database.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print("Creating unified car_complete view...\n")

# Remove old version if it exists
cursor.execute("DROP VIEW IF EXISTS car_complete;")

cursor.execute("""
CREATE VIEW car_complete AS
SELECT

    -- ==============================
    -- MASTER INFORMATION
    -- ==============================

    m.car_id,
    m.brand,
    m.model,
    m.variant_trim,
    m.body_type,
    m.launch_year,
    m.segment,

    -- ==============================
    -- ENGINE
    -- ==============================

    e.engine_type,
    e.displacement_cc,
    e.cylinders,
    e.transmission_type,
    e.drivetrain,

    -- ==============================
    -- PERFORMANCE
    -- ==============================

    pp.power_ps,
    pp.torque_nm,
    pp.accel_0_100_sec,
    pp.top_speed_kmh,
    pp.fuel_efficiency_kmpl,

    -- ==============================
    -- PRICE
    -- ==============================

    p.ex_showroom_min_inr_lakh,
    p.ex_showroom_max_inr_lakh,
    p.top_variant_price_inr_lakh,
    p.currency,
    p.price_as_of_date,

    -- ==============================
    -- SAFETY
    -- ==============================

    s.ncap_rating_stars,
    s.ncap_body,
    s.airbags_count,
    s.adas_available,
    s.abs_esc_available,

    -- ==============================
    -- DIMENSIONS
    -- ==============================

    d.length_mm,
    d.width_mm,
    d.height_mm,
    d.wheelbase_mm,
    d.boot_space_litres,

    -- ==============================
    -- RATINGS
    -- ==============================

    r.expert_rating_out_of_10,
    r.user_rating_out_of_5,
    r.review_count

FROM master_overview AS m

LEFT JOIN engine_configuration AS e
    ON m.car_id = e.car_id

LEFT JOIN power_performance AS pp
    ON m.car_id = pp.car_id

LEFT JOIN price AS p
    ON m.car_id = p.car_id

LEFT JOIN safety AS s
    ON m.car_id = s.car_id

LEFT JOIN dimensions AS d
    ON m.car_id = d.car_id

LEFT JOIN ratings_reviews AS r
    ON m.car_id = r.car_id;
""")

conn.commit()

# ==============================
# VERIFY VIEW
# ==============================

cursor.execute("""
SELECT COUNT(*)
FROM car_complete;
""")

count = cursor.fetchone()[0]

print("car_complete created successfully!")
print(f"Cars available: {count}")

# Count columns
cursor.execute("PRAGMA table_info(car_complete);")
columns = cursor.fetchall()

print(f"Columns available: {len(columns)}")

print("\nColumns:")
for column in columns:
    print(f"  - {column[1]} ({column[2]})")

conn.close()