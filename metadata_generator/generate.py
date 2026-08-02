"""
metadata_generator/generate.py
"""

from pathlib import Path

from metadata_generator.inspector import SQLiteInspector
from metadata_generator.statistics import StatisticsBuilder
from metadata_generator.validator import MetadataValidator
from metadata_generator.json_writer import JSONWriter
from metadata_generator.markdown import MarkdownWriter


ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "car_specs_database.db"
METADATA_DIR = ROOT / "metadata"


def main():

    metadata = {
        "database": {
            "name": "Indian Passenger Vehicle Database",
            "dialect": "SQLite",
            "domain": "Automotive",
            "primary_entity": "Vehicle",
            "primary_key": "car_id",
            "default_view": "car_complete",
        },
        "tables": {},
        "views": {},
    }

    inspector = SQLiteInspector(str(DB_PATH))
    builder = StatisticsBuilder(inspector)

    print("Reading database...")

    for table in inspector.get_tables():
        print(f"Processing table: {table}")
        metadata["tables"][table] = builder.build_table_metadata(table)

    for view in inspector.get_views():
        metadata["views"][view] = {
            "description": "Database view",
            "recommended": True,
        }

    validator = MetadataValidator()
    validator.validate(metadata)
    validator.print_summary(metadata)

    JSONWriter.write(
        metadata,
        METADATA_DIR / "schema_metadata_v3.json",
    )

    MarkdownWriter.write_summary(
        metadata,
        METADATA_DIR / "schema_summary.md",
    )

    MarkdownWriter.write_dictionary(
        metadata,
        METADATA_DIR / "database_dictionary.md",
    )

    inspector.close()

    print("\nMetadata generation completed successfully!")
    print(f"Output folder: {METADATA_DIR}")


if __name__ == "__main__":
    main()