from dataclasses import dataclass

DATABASE_NAME = "Indian Passenger Vehicle Database"

DATABASE_VERSION = "3.0"

DOMAIN = "Automotive"

PRIMARY_ENTITY = "Vehicle"

PRIMARY_KEY = "car_id"

DEFAULT_VIEW = "car_complete"

DATABASE_DESCRIPTION = """
Automotive relational database containing passenger vehicle
specifications, pricing, dimensions, safety ratings,
performance metrics and expert reviews.
"""

SUPPORTED_DIALECT = "SQLite"


@dataclass
class ColumnRule:

    semantic_type: str

    unit: str | None = None

    better_when: str | None = None

    sortable: bool = True

    filterable: bool = True

    aggregatable: bool = True