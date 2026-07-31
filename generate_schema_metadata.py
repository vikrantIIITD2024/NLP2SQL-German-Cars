import sqlite3
import json

DB = "car_specs_database.db"

# --------------------------------------------------------------------
# Human-written descriptions
# --------------------------------------------------------------------

COLUMN_DESCRIPTIONS = {

    "master_overview": {

        "car_id":"Unique identifier of each vehicle.",
        "brand":"Vehicle manufacturer.",
        "model":"Vehicle model.",
        "variant_trim":"Vehicle variant or trim.",
        "body_type":"SUV, Sedan, Hatchback etc.",
        "launch_year":"Year of launch.",
        "segment":"Vehicle market segment."

    },

    "engine_configuration":{

        "engine_type":"Fuel type / engine technology.",
        "displacement_cc":"Engine displacement in cubic centimetres.",
        "cylinders":"Number of engine cylinders.",
        "transmission_type":"Transmission type.",
        "drivetrain":"Drive configuration."

    },

    "power_performance":{

        "power_ps":"Maximum engine power (PS).",
        "torque_nm":"Maximum torque (Nm).",
        "accel_0_100_sec":"Time to accelerate from 0 to 100 km/h.",
        "top_speed_kmh":"Maximum speed.",
        "fuel_efficiency_kmpl":"Claimed fuel efficiency."

    },

    "price":{

        "ex_showroom_min_inr_lakh":"Starting ex-showroom price.",
        "ex_showroom_max_inr_lakh":"Maximum ex-showroom price.",
        "top_variant_price_inr_lakh":"Price of top variant.",
        "currency":"Currency.",
        "price_as_of_date":"Date when price was recorded."

    },

    "safety":{

        "ncap_rating_stars":"NCAP safety rating.",
        "ncap_body":"Testing organization.",
        "airbags_count":"Number of airbags.",
        "adas_available":"Whether ADAS is available.",
        "abs_esc_available":"Whether ABS and ESC are available."

    },

    "dimensions":{

        "length_mm":"Vehicle length.",
        "width_mm":"Vehicle width.",
        "height_mm":"Vehicle height.",
        "wheelbase_mm":"Wheelbase.",
        "boot_space_litres":"Boot capacity."

    },

    "ratings_reviews":{

        "expert_rating_out_of_10":"Expert rating.",
        "user_rating_out_of_5":"Average user rating.",
        "review_count":"Number of user reviews."

    }

}

# --------------------------------------------------------------------

conn = sqlite3.connect(DB)

cursor = conn.cursor()

tables = cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
AND name NOT LIKE 'sqlite_%';
ORDER BY name;
""").fetchall()

schema = {}

for (table,) in tables:

    info = cursor.execute(
        f"PRAGMA table_info('{table}')"
    ).fetchall()

    fk = cursor.execute(
        f"PRAGMA foreign_key_list('{table}')"
    ).fetchall()

    schema[table] = {

        "primary_key":None,
        "foreign_keys":[],
        "columns":[]

    }

    for row in info:

        cid,name,dtype,notnull,default,pk=row

        if pk:
            schema[table]["primary_key"]=name

        schema[table]["columns"].append({

            "name":name,
            "type":dtype,
            "nullable":not bool(notnull),
            "description":COLUMN_DESCRIPTIONS.get(table,{}).get(name,"")

        })

    for f in fk:

        schema[table]["foreign_keys"].append({

            "column":f[3],
            "references":f[2]+"."+f[4]

        })

with open("schema_metadata.json","w") as f:

    json.dump(schema,f,indent=4)

conn.close()

print("schema_metadata.json generated successfully.")