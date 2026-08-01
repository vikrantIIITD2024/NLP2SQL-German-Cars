
"""
metadata_generator/json_writer.py
"""

import json
from pathlib import Path

class JSONWriter:
    @staticmethod
    def write(metadata: dict, output_path: str):
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4, ensure_ascii=False)

        print(f"[OK] JSON written to {output}")
