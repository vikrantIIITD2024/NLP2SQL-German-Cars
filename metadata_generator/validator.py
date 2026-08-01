
"""
metadata_generator/validator.py

Validates generated schema metadata before writing to disk.
"""

from typing import Dict, Any


class MetadataValidator:
    REQUIRED_DATABASE_KEYS = [
        "name",
        "dialect",
        "domain",
        "primary_entity",
        "primary_key",
    ]

    REQUIRED_COLUMN_KEYS = [
        "name",
        "datatype",
        "semantic_type",
        "nullable",
    ]

    def validate(self, metadata: Dict[str, Any]) -> None:
        """Raise ValueError if metadata is invalid."""
        self._validate_database(metadata)
        self._validate_tables(metadata)
        self._validate_views(metadata)

    def _validate_database(self, metadata: Dict[str, Any]) -> None:
        if "database" not in metadata:
            raise ValueError("Missing 'database' section.")

        db = metadata["database"]

        for key in self.REQUIRED_DATABASE_KEYS:
            if key not in db:
                raise ValueError(f"Missing database key: {key}")

    def _validate_tables(self, metadata: Dict[str, Any]) -> None:
        if "tables" not in metadata:
            raise ValueError("Missing 'tables' section.")

        table_names = set()

        for table_name, table in metadata["tables"].items():

            if table_name in table_names:
                raise ValueError(f"Duplicate table: {table_name}")

            table_names.add(table_name)

            if "columns" not in table:
                raise ValueError(f"{table_name}: missing columns")

            seen_columns = set()

            for column in table["columns"]:

                for key in self.REQUIRED_COLUMN_KEYS:
                    if key not in column:
                        raise ValueError(
                            f"{table_name}.{column.get('name','?')} missing '{key}'"
                        )

                col_name = column["name"]

                if col_name in seen_columns:
                    raise ValueError(
                        f"Duplicate column '{col_name}' in table '{table_name}'"
                    )

                seen_columns.add(col_name)

                stats = column.get("statistics")
                if stats:
                    if not isinstance(stats, dict):
                        raise ValueError(
                            f"{table_name}.{col_name}: statistics must be a dictionary."
                        )

    def _validate_views(self, metadata: Dict[str, Any]) -> None:
        views = metadata.get("views", {})

        if not isinstance(views, dict):
            raise ValueError("'views' must be a dictionary.")

    def print_summary(self, metadata: Dict[str, Any]) -> None:
        print("=" * 60)
        print("Metadata Validation Successful")
        print("=" * 60)
        print("Tables :", len(metadata.get("tables", {})))
        print("Views  :", len(metadata.get("views", {})))

        total_columns = 0
        for table in metadata.get("tables", {}).values():
            total_columns += len(table.get("columns", []))

        print("Columns:", total_columns)
        print("=" * 60)
