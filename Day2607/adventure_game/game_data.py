rooms = {
    "forest": {
        "desc": "You are in a dark forest. Paths lead north and east.",
        "items": ["stick"],
        "exits": {"north": "cave", "east": "village"}
    },
    "cave": {
        "desc": "A damp cave. You hear growling deeper inside.",
        "items": ["torch"],
        "enemy": "goblin",
        "exits": {"south": "forest"}
    },
    "village": {
        "desc": "A quiet village. The townspeople are scared.",
        "items": [],
        "exits": {"west": "forest", "north": "castle"}
    },
    "castle": {
        "desc": "An abandoned castle. A dragon sleeps here.",
        "enemy": "dragon",
        "items": ["treasure"],
        "exits": {"south": "village"}
    }
}

enemies = {
    "goblin": {"hp": 20, "damage": 5},
    "dragon": {"hp": 50, "damage": 15}
}
