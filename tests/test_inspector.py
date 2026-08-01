from metadata_generator.inspector import SQLiteInspector

db = SQLiteInspector("database/car_specs_database.db")

print("Tables")
print(db.get_tables())

print()

print("Views")
print(db.get_views())

print()

for table in db.get_tables():

    print("=" * 60)

    print(table)

    print("Rows:", db.get_row_count(table))

    print()

    print("Columns")

    for c in db.get_columns(table):

        print(c)

db.close()