import json
from game_data import rooms, enemies

player = {
    "location": "forest",
    "inventory": [],
    "health": 100
}

def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player, f)
    print("💾 Game saved.")

def load_game():
    global player
    try:
        with open("savegame.json", "r") as f:
            player = json.load(f)
        print("📂 Game loaded.")
    except FileNotFoundError:
        print("⚠️ No saved game found.")

def show_status():
    print(f"\n📍 Location: {player['location'].title()}")
    print(f"❤️ Health: {player['health']}")
    print(f"🎒 Inventory: {player['inventory']}")
    print("🧭 " + rooms[player["location"]]["desc"])

def move(direction):
    loc = player["location"]
    if direction in rooms[loc]["exits"]:
        player["location"] = rooms[loc]["exits"][direction]
        print(f"➡️ Moved to {player['location'].title()}")
    else:
        print("❌ Can't go that way.")

def pickup():
    loc = player["location"]
    items = rooms[loc].get("items", [])
    if items:
        for item in items:
            player["inventory"].append(item)
        rooms[loc]["items"] = []
        print(f"✅ Picked up: {', '.join(items)}")
    else:
        print("👜 Nothing to pick up here.")

def fight():
    loc = player["location"]
    enemy = rooms[loc].get("enemy")
    if not enemy:
        print("🕊️ Nothing to fight here.")
        return

    stats = enemies[enemy]
    print(f"⚔️ A wild {enemy} appears!")

    while stats["hp"] > 0 and player["health"] > 0:
        stats["hp"] -= 10
        player["health"] -= stats["damage"]
        print(f"🗡️ You hit the {enemy}. Enemy HP: {stats['hp']}")
        print(f"💥 You got hit! Your HP: {player['health']}")

    if player["health"] <= 0:
        print("☠️ You died. Game over.")
        exit()
    else:
        print(f"🏆 You defeated the {enemy}!")
        del rooms[loc]["enemy"]

def check_endings():
    if "treasure" in player["inventory"] and player["location"] == "forest":
        print("🎉 You escaped the forest with treasure. You win!")
        exit()

def main():
    print("🧙 Welcome to the Adventure Game!")

    while True:
        show_status()
        print("\nActions: move [dir] | pickup | fight | save | load | quit")
        command = input(">>> ").strip().lower()

        if command.startswith("move"):
            _, direction = command.split()
            move(direction)
        elif command == "pickup":
            pickup()
        elif command == "fight":
            fight()
        elif command == "save":
            save_game()
        elif command == "load":
            load_game()
        elif command == "quit":
            print("👋 Goodbye!")
            break
        else:
            print("❓ Invalid command.")

        check_endings()

if __name__ == "__main__":
    main()
