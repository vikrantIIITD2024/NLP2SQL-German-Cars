import sqlite3
import json
import pandas as pd

DB = "car_specs_database.db"

conn = sqlite3.connect(DB)

# -----------------------------------------
# Manual metadata
# -----------------------------------------

TABLE_DESCRIPTIONS = {

    "master_overview": {
        "description":"Master table containing one record per vehicle.",
        "purpose":"Acts as the parent table for all vehicle information."
    },

    "engine_configuration":{
        "description":"Engine and drivetrain specifications.",
        "purpose":"Stores engine architecture and transmission."
    },

    "power_performance":{
        "description":"Vehicle performance specifications.",
        "purpose":"Used for power, acceleration and mileage queries."
    },

    "price":{
        "description":"Vehicle pricing.",
        "purpose":"Stores ex-showroom pricing."
    },

    "dimensions":{
        "description":"Vehicle dimensions.",
        "purpose":"Stores physical measurements."
    },

    "safety":{
        "description":"Vehicle safety information.",
        "purpose":"Stores NCAP ratings and safety features."
    },

    "ratings_reviews":{
        "description":"Vehicle ratings.",
        "purpose":"Stores expert and user ratings."
    }

}

UNITS = {

    "displacement_cc":"cc",
    "power_ps":"PS",
    "torque_nm":"Nm",
    "accel_0_100_sec":"seconds",
    "top_speed_kmh":"km/h",
    "fuel_efficiency_kmpl":"km/l",

    "length_mm":"mm",
    "width_mm":"mm",
    "height_mm":"mm",
    "wheelbase_mm":"mm",

    "boot_space_litres":"litres",

    "ex_showroom_min_inr_lakh":"INR lakh",
    "ex_showroom_max_inr_lakh":"INR lakh",
    "top_variant_price_inr_lakh":"INR lakh"

}

SEMANTIC_TYPES = {

    "brand":"categorical",
    "model":"categorical",
    "segment":"categorical",
    "body_type":"categorical",
    "engine_type":"categorical",
    "transmission_type":"categorical",
    "drivetrain":"categorical",

    "launch_year":"year",

    "currency":"currency",

    "expert_rating_out_of_10":"rating",
    "user_rating_out_of_5":"rating"

}

GLOSSARY = {

    "ADAS":"Advanced Driver Assistance Systems",

    "ABS":"Anti-lock Braking System",

    "ESC":"Electronic Stability Control",

    "PS":"Metric Horsepower",

    "Nm":"Newton metre",

    "NCAP":"New Car Assessment Programme"

}

# -----------------------------------------
# Database Metadata
# -----------------------------------------

schema = {

    "database":{

        "name":"Indian Car Specifications",

        "dialect":"SQLite",

        "description":"Relational automotive database of passenger vehicles.",

        "primary_entity":"Vehicle",

        "join_key":"car_id"

    },

    "glossary":GLOSSARY,

    "join_information":{

        "primary_join_key":"car_id",

        "relationship":"one_to_one"

    },

    "tables":{},

    "views":{

        "car_complete":{

            "description":"Flattened vehicle view for Text-to-SQL.",

            "purpose":"Allows simple SQL generation without joins."

        }

    }

}

# -----------------------------------------
# Read Tables
# -----------------------------------------

tables = pd.read_sql("""

SELECT name

FROM sqlite_master

WHERE type='table'

AND name NOT LIKE 'sqlite_%'

ORDER BY name;

""", conn)

for table in tables["name"]:

    info = pd.read_sql(f"PRAGMA table_info({table})", conn)

    fk = pd.read_sql(f"PRAGMA foreign_key_list({table})", conn)

    table_json = {

        "description":TABLE_DESCRIPTIONS.get(table,{}).get("description",""),

        "purpose":TABLE_DESCRIPTIONS.get(table,{}).get("purpose",""),

        "primary_key":None,

        "foreign_keys":[],

        "relationships":[],

        "query_hints":[

            "Join using car_id",

            "Can be filtered",

            "Can be aggregated"

        ],

        "columns":[]

    }

    for _,row in info.iterrows():

        col=row["name"]

        dtype=row["type"]

        pk=bool(row["pk"])

        nullable=not bool(row["notnull"])

        if pk:

            table_json["primary_key"]=col

        examples=[]

        try:

            q=f"""

            SELECT DISTINCT "{col}"

            FROM {table}

            WHERE "{col}" IS NOT NULL

            LIMIT 5

            """

            examples=pd.read_sql(q,conn)[col].tolist()

        except:

            pass

        stats=None

        if dtype in ["INTEGER","REAL"]:

            try:

                q=f"""

                SELECT

                    MIN("{col}") as min,

                    MAX("{col}") as max

                FROM {table}

                """

                s=pd.read_sql(q,conn)

                stats={

                    "min":s.iloc[0]["min"],

                    "max":s.iloc[0]["max"]

                }

            except:

                pass

        table_json["columns"].append({

            "name":col,

            "datatype":dtype,

            "nullable":nullable,

            "semantic_type":SEMANTIC_TYPES.get(col,"numeric" if dtype in ["INTEGER","REAL"] else "text"),

            "unit":UNITS.get(col,None),

            "examples":examples,

            "statistics":stats

        })

    for _,r in fk.iterrows():

        table_json["foreign_keys"].append({

            "column":r["from"],

            "references":r["table"]+"."+r["to"]

        })

        table_json["relationships"].append({

            "type":"one_to_one",

            "join":f'{table}.{r["from"]} = {r["table"]}.{r["to"]}'

        })

    schema["tables"][table]=table_json

# -----------------------------------------

import numpy as np

def json_converter(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

with open("schema_metadata_v2.json", "w") as f:
    json.dump(
        schema,
        f,
        indent=4,
        default=json_converter
    )

conn.close()

print("schema_metadata_v2.json created.")