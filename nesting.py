capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Germany": "Berlin"
}

nested_dict = {
    "Key": [capitals],
    "Dict": {}
}

travel_log = {
    "USA": ["New York City", "Boston"],
    "Germany": ["Berlin", "Munich"],
    "France": ["Paris"]
}

travel_visits = {
    "France": {"Cities_visited": ["Paris", "Lille", "Lyon"]},
    "Germany": {
        "Cities_visited": {
            "North_Germany": ["Hamburg", "Bremen"],
            "total_visits": "12"
        }
    }
}

travel_log = [{
    {"country": "France", 
     "cities_visited": ["Paris", "Lille", "Lyon"], 
     "total_visits": "12"
     },
    {"country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": "12"}
},
]