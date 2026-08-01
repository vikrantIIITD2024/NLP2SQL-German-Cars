
"""
metadata_generator/statistics.py
"""

from typing import Any, Dict
from .automotive import COLUMN_RULES

class StatisticsBuilder:
    def __init__(self, inspector):
        self.inspector = inspector

    def build_table_metadata(self, table:str)->Dict[str,Any]:
        cols=self.inspector.get_columns(table)
        fks=self.inspector.get_foreign_keys(table)
        pk=None
        for c in cols:
            if c["pk"]:
                pk=c["name"]
                break
        return {
            "description": table.replace("_"," ").title(),
            "row_count": self.inspector.get_row_count(table),
            "primary_key": pk,
            "foreign_keys":[
                {"column":fk["from"],"references":f"{fk['table']}.{fk['to']}"}
                for fk in fks
            ],
            "columns":[self.build_column_metadata(table,c) for c in cols]
        }

    def build_column_metadata(self, table:str, column:Dict[str,Any])->Dict[str,Any]:
        name=column["name"]
        dtype=column["type"]
        numeric=self.inspector.is_numeric(dtype)
        rule=COLUMN_RULES.get(name,{})
        return {
            "name":name,
            "datatype":dtype,
            "nullable": not bool(column["notnull"]),
            "semantic_type": rule.get("semantic_type", self._infer(name,dtype)),
            "description": name.replace("_"," ").capitalize()+".",
            "unit": rule.get("unit"),
            "better_when": rule.get("better_when"),
            "sortable": numeric,
            "filterable": True,
            "aggregatable": numeric,
            "examples": self.inspector.get_examples(table,name),
            "distinct_values": self.inspector.get_distinct_values(table,name),
            "statistics": self.inspector.get_numeric_stats(table,name) if numeric else None,
            "user_phrases": self._phrases(name)
        }

    def _infer(self,name,dtype):
        n=name.lower()
        if "price" in n: return "price"
        if "rating" in n: return "rating"
        if "year" in n: return "year"
        if "power" in n or "torque" in n: return "performance"
        if "fuel" in n or "kmpl" in n: return "fuel_economy"
        if dtype.upper() in ("INTEGER","REAL","FLOAT","NUMERIC"):
            return "numeric"
        return "categorical"

    def _phrases(self,name):
        return {
            "power_ps":["horsepower","hp","engine power"],
            "fuel_efficiency_kmpl":["mileage","fuel economy","fuel efficiency"],
            "top_variant_price_inr_lakh":["price","cost","budget"],
            "ncap_rating_stars":["safety","crash rating","NCAP"],
            "boot_space_litres":["boot","trunk","cargo space"]
        }.get(name,[])
