import sqlite3
from typing import Dict, List


class SQLiteInspector:

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    # ----------------------------------------------------
    # Database
    # ----------------------------------------------------

    def get_tables(self) -> List[str]:

        cur = self.conn.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """)

        return [row["name"] for row in cur.fetchall()]

    def get_views(self) -> List[str]:

        cur = self.conn.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='view'
            ORDER BY name;
        """)

        return [row["name"] for row in cur.fetchall()]

    # ----------------------------------------------------
    # Table Metadata
    # ----------------------------------------------------

    def get_columns(self, table: str):

        cur = self.conn.execute(
            f"PRAGMA table_info('{table}')"
        )

        return [dict(r) for r in cur.fetchall()]

    def get_foreign_keys(self, table: str):

        cur = self.conn.execute(
            f"PRAGMA foreign_key_list('{table}')"
        )

        return [dict(r) for r in cur.fetchall()]

    def get_indexes(self, table: str):

        cur = self.conn.execute(
            f"PRAGMA index_list('{table}')"
        )

        return [dict(r) for r in cur.fetchall()]

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    def get_row_count(self, table):

        cur = self.conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        return cur.fetchone()[0]

    def get_distinct_values(
            self,
            table,
            column,
            limit=25
    ):

        query = f"""
        SELECT DISTINCT "{column}"
        FROM "{table}"
        WHERE "{column}" IS NOT NULL
        ORDER BY "{column}"
        LIMIT {limit}
        """

        try:

            cur = self.conn.execute(query)

            return [r[0] for r in cur.fetchall()]

        except:

            return []

    def get_examples(
            self,
            table,
            column,
            limit=5
    ):

        query = f"""
        SELECT "{column}"
        FROM "{table}"
        WHERE "{column}" IS NOT NULL
        LIMIT {limit}
        """

        try:

            cur = self.conn.execute(query)

            return [r[0] for r in cur.fetchall()]

        except:

            return []

    def get_numeric_stats(
            self,
            table,
            column
    ):

        query = f"""
        SELECT
            MIN("{column}") AS min_value,
            MAX("{column}") AS max_value,
            AVG("{column}") AS avg_value
        FROM "{table}"
        """

        try:

            row = self.conn.execute(query).fetchone()

            return {

                "min": row["min_value"],
                "max": row["max_value"],
                "average": row["avg_value"]

            }

        except:

            return None

    # ----------------------------------------------------
    # Helpers
    # ----------------------------------------------------

    def is_numeric(self, sqlite_type):

        sqlite_type = sqlite_type.upper()

        return sqlite_type in (

            "INTEGER",

            "REAL",

            "FLOAT",

            "NUMERIC"

        )