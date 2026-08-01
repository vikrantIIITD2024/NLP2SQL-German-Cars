import sqlite3
import pandas as pd
import re

EXCEL_FILE = "car_specs_database.xlsx"
DB_FILE = "car_specs_database.db"

conn = sqlite3.connect(DB_FILE)
conn.execute("PRAGMA foreign_keys = ON;")

xls = pd.ExcelFile(EXCEL_FILE)

# -----------------------------------
# Utility
# -----------------------------------

def clean(name):
    name = str(name).strip().lower()
    name = re.sub(r"[^\w]", "_", name)
    name = re.sub("_+", "_", name)
    return name


def sqlite_type(series):
    if pd.api.types.is_integer_dtype(series):
        return "INTEGER"

    if pd.api.types.is_float_dtype(series):
        return "REAL"

    return "TEXT"


# -----------------------------------
# First create Master table
# -----------------------------------

master = pd.read_excel(EXCEL_FILE, sheet_name="Master_Overview")

master.columns = [clean(c) for c in master.columns]

master = master.dropna(how="all")
master = master.dropna(axis=1, how="all")

columns = []

for col in master.columns:

    dtype = sqlite_type(master[col])

    if col == "car_id":
        columns.append(f"{col} TEXT PRIMARY KEY")
    else:
        columns.append(f"{col} {dtype}")

create_sql = f"""
CREATE TABLE master_overview(
{','.join(columns)}
);
"""

conn.execute("DROP TABLE IF EXISTS master_overview")
conn.execute(create_sql)

master.to_sql(
    "master_overview",
    conn,
    if_exists="append",
    index=False,
)

print("Created master_overview")

# -----------------------------------
# Remaining tables
# -----------------------------------

for sheet in xls.sheet_names:

    if sheet in ["ReadMe", "Master_Overview"]:
        continue

    print("Creating", sheet)

    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet)

    df.columns = [clean(c) for c in df.columns]

    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    table = clean(sheet)

    conn.execute(f"DROP TABLE IF EXISTS {table}")

    sql = []

    for col in df.columns:

        dtype = sqlite_type(df[col])

        if col == "car_id":
            sql.append("car_id TEXT NOT NULL")
        else:
            sql.append(f"{col} {dtype}")

    sql.append("""
FOREIGN KEY(car_id)
REFERENCES master_overview(car_id)
ON UPDATE CASCADE
ON DELETE CASCADE
""")

    create = f"""
CREATE TABLE {table}(
{','.join(sql)}
);
"""

    conn.execute(create)

    df.to_sql(
        table,
        conn,
        if_exists="append",
        index=False,
    )

    conn.execute(
        f"CREATE INDEX idx_{table}_car_id ON {table}(car_id);"
    )

conn.commit()

# -----------------------------------
# Verify
# -----------------------------------

print("\nTables")

tables = conn.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""")

for t in tables.fetchall():
    print("•", t[0])

print("\nForeign Keys\n")

for t in conn.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
"""):

    table = t[0]

    fk = conn.execute(f"PRAGMA foreign_key_list('{table}')").fetchall()

    if fk:
        print(table, fk)

conn.close()

print("\nDatabase successfully created!")