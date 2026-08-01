
"""
metadata_generator/generate.py
"""

from pathlib import Path

from inspector import SQLiteInspector
from statistics import StatisticsBuilder
from validator import MetadataValidator
from json_writer import JSONWriter
from markdown import MarkdownWriter

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "car_specs_database.db"
METADATA_DIR = ROOT / "metadata"

metadata = {
    "database": {
        "name": "Indian Passenger Vehicle Database",
        "dialect": "SQLite",
        "domain": "Automotive",
        "primary_entity": "Vehicle",
        "primary_key": "car_id",
        "default_view": "car_complete"
    },
    "tables": {},
    "views": {}
}

inspector = SQLiteInspector(str(DB_PATH))
builder = StatisticsBuilder(inspector)

for table in inspector.get_tables():
    metadata["tables"][table] = builder.build_table_metadata(table)

for view in inspector.get_views():
    metadata["views"][view] = {
        "description": "Database view",
        "recommended": True
    }

validator = MetadataValidator()
validator.validate(metadata)
validator.print_summary(metadata)

JSONWriter.write(
    metadata,
    str(METADATA_DIR / "schema_metadata_v3.json")
)

MarkdownWriter.write_summary(
    metadata,
    str(METADATA_DIR / "schema_summary.md")
)

MarkdownWriter.write_dictionary(
    metadata,
    str(METADATA_DIR / "database_dictionary.md")
)

inspector.close()

print("\nMetadata generation complete.")
