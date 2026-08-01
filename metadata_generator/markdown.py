
"""
metadata_generator/markdown.py
"""

from pathlib import Path

class MarkdownWriter:

    @staticmethod
    def write_summary(metadata: dict, output_path: str):
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        with open(out, "w", encoding="utf-8") as f:
            db = metadata["database"]
            f.write("# Schema Summary\n\n")
            f.write(f"**Database:** {db['name']}\n\n")
            f.write(f"**Domain:** {db['domain']}\n\n")
            f.write("## Tables\n\n")
            for name, table in metadata["tables"].items():
                f.write(f"### {name}\n")
                f.write(f"- Rows: {table['row_count']}\n")
                f.write(f"- Columns: {len(table['columns'])}\n\n")

    @staticmethod
    def write_dictionary(metadata: dict, output_path: str):
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        with open(out, "w", encoding="utf-8") as f:
            f.write("# Database Dictionary\n\n")
            for table_name, table in metadata["tables"].items():
                f.write(f"## {table_name}\n\n")
                for col in table["columns"]:
                    f.write(f"### {col['name']}\n")
                    f.write(f"- Type: {col['datatype']}\n")
                    f.write(f"- Semantic: {col['semantic_type']}\n")
                    if col.get("unit"):
                        f.write(f"- Unit: {col['unit']}\n")
                    f.write(f"- Description: {col['description']}\n\n")
