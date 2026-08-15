"""
few_shot_generator/templates.py

Natural language templates used for generating
few-shot Question → SQL examples.
"""

QUESTION_TEMPLATES = {

    # ==========================================================
    # BRAND
    # ==========================================================

    "brand": [

        "Show all {brand} cars",

        "List all {brand} vehicles",

        "Display every {brand} model",

        "Which cars does {brand} sell?",

        "Give me all {brand} cars",

        "Show me the complete {brand} lineup",

        "List every vehicle manufactured by {brand}",

        "Which {brand} models are available?",

        "Display all vehicles from {brand}",

        "Show all cars made by {brand}"

    ],

    # ==========================================================
    # MODEL
    # ==========================================================

    "model": [

        "Show details of {model}",

        "Display specifications of {model}",

        "Tell me about {model}",

        "Give me complete information about {model}",

        "Show every specification of {model}",

        "Show {model} details"

    ],

    # ==========================================================
    # PRICE
    # ==========================================================

    "price": [

        "Cars under {price} lakh",

        "Cars below {price} lakh",

        "Vehicles cheaper than {price} lakh",

        "Cars costing less than {price} lakh",

        "Cars above {price} lakh",

        "Vehicles over {price} lakh",

        "Cars between {min_price} and {max_price} lakh",

        "Most expensive car",

        "Cheapest car",

        "Most expensive {brand}",

        "Cheapest {brand}",

        "Top 5 most expensive cars",

        "Top 10 cheapest cars"

    ],

    # ==========================================================
    # PERFORMANCE
    # ==========================================================

    "performance": [

        "Most powerful car",

        "Most powerful {brand}",

        "Cars with more than {power} PS",

        "Cars producing over {power} horsepower",

        "Highest horsepower vehicle",

        "Cars with torque above {torque} Nm",

        "Fastest car",

        "Highest top speed",

        "Best acceleration"

    ],

    # ==========================================================
    # FUEL ECONOMY
    # ==========================================================

    "mileage": [

        "Highest mileage car",

        "Most fuel efficient vehicle",

        "Best mileage SUV",

        "Best mileage sedan",

        "Highest mileage {brand}",

        "Cars with mileage above {mileage} kmpl",

        "Fuel efficient automatic cars",

        "Most economical car"

    ],

    # ==========================================================
    # BODY TYPE
    # ==========================================================

    "body_type": [

        "Show all {body_type}",

        "List every {body_type}",

        "{body_type} under {price} lakh",

        "Most powerful {body_type}",

        "Highest mileage {body_type}",

        "Safest {body_type}"

    ],

    # ==========================================================
    # ENGINE
    # ==========================================================

    "engine": [

        "{engine_type} cars",

        "{engine_type} SUVs",

        "{engine_type} sedans",

        "Automatic {engine_type} cars",

        "Manual {engine_type} cars",

        "{engine_type} vehicles under {price} lakh"

    ],

    # ==========================================================
    # TRANSMISSION
    # ==========================================================

    "transmission": [

        "Automatic cars",

        "Manual cars",

        "Automatic SUVs",

        "Manual sedans",

        "Automatic cars under {price} lakh"

    ],

    # ==========================================================
    # SAFETY
    # ==========================================================

    "safety": [

        "Cars with ADAS",

        "Cars with 6 airbags",

        "Cars with more than {airbags} airbags",

        "5 star NCAP cars",

        "Safest car",

        "Safest SUV",

        "Cars with ABS",

        "Cars with ESC"

    ],

    # ==========================================================
    # DIMENSIONS
    # ==========================================================

    "dimensions": [

        "Longest car",

        "Shortest car",

        "Largest boot space",

        "Cars with boot space above {boot} litres",

        "Longest wheelbase",

        "Tallest SUV",

        "Widest sedan"

    ],

    # ==========================================================
    # RATINGS
    # ==========================================================

    "ratings": [

        "Highest rated car",

        "Best expert rated vehicle",

        "Best user rated car",

        "Cars with expert rating above {rating}",

        "Most reviewed car",

        "Top rated SUV"

    ],

    # ==========================================================
    # AGGREGATION
    # ==========================================================

    "aggregation": [

        "Average mileage",

        "Average price",

        "Average power",

        "Average mileage of {brand}",

        "Average price of {brand}",

        "Count all SUVs",

        "Number of BMW cars",

        "How many automatic cars are there?",

        "How many diesel SUVs are available?"

    ],

    # ==========================================================
    # COMPARISON
    # ==========================================================

    "comparison": [

        "Compare BMW and Audi prices",

        "Compare Volkswagen and Skoda mileage",

        "Compare SUV and Sedan prices",

        "Compare petrol and diesel mileage",

        "Which brand has the highest average mileage?",

        "Which brand has the most powerful cars?"

    ],

    # ==========================================================
    # COMBINED
    # ==========================================================

    "combined": [

        "{brand} SUV under {price} lakh",

        "{brand} sedan over {power} PS",

        "{engine_type} automatic SUV",

        "{engine_type} manual hatchback",

        "Cars under {price} lakh with ADAS",

        "{brand} cars with mileage above {mileage} kmpl",

        "{brand} automatic SUV with 6 airbags",

        "Petrol sedan with highest mileage",

        "Diesel SUV with highest power"

    ]

}