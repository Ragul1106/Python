import json
import random
import os
from functools import wraps
from typing import Dict, List, Generator, Optional

class Player:
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.max_health = health
        self.health = health
        self.inventory: List[str] = []
        self.current_scene = "start"
    
    def add_to_inventory(self, item: str) -> None:
        """Add an item to the player's inventory"""
        self.inventory.append(item)
        print(f"\nYou acquired: {item}")
    
    def take_damage(self, amount: int) -> None:
        """Reduce player's health by specified amount"""
        self.health = max(0, self.health - amount)
        print(f"\nYou took {amount} damage! Health: {self.health}/{self.max_health}")
        if self.health <= 0:
            print("\nYou have been defeated!")
    
    def heal(self, amount: int) -> None:
        """Restore player's health by specified amount"""
        self.health = min(self.max_health, self.health + amount)
        print(f"\nYou healed {amount} health! Health: {self.health}/{self.max_health}")
    
    def has_item(self, item: str) -> bool:
        """Check if player has a specific item"""
        return item in self.inventory
    
    def display_status(self) -> None:
        """Show player's current status"""
        print(f"\n=== {self.name} ===")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("=================")

class Scene:
    def __init__(self, scene_id: str, description: str, choices: Dict[str, str], enemy: Optional[Dict] = None, item: Optional[str] = None):
        self.scene_id = scene_id
        self.description = description
        self.choices = choices  
        self.enemy = enemy  
        self.item = item
    
    def display(self) -> None:
        """Display the scene description and available choices"""
        print(f"\n{self.description}")
        
        if self.enemy:
            print(f"\nA wild {self.enemy['name']} appears! (Health: {self.enemy['health']}, Damage: {self.enemy['damage']})")
        
        if self.item and not self.item.startswith("_"):
            print(f"\nYou notice a {self.item} here.")
        
        print("\nAvailable actions:")
        for i, (choice, target) in enumerate(self.choices.items(), 1):
            print(f"{i}. {choice}")
        
        if self.enemy:
            print(f"{len(self.choices)+1}. Attack the {self.enemy['name']}")
            print(f"{len(self.choices)+2}. Try to flee")

class Game:
    def __init__(self):
        self.player: Optional[Player] = None
        self.scenes: Dict[str, Scene] = {}
        self.game_file = "rpg_save.json"
        self.setup_game()
    
    def setup_game(self) -> None:
        """Initialize game scenes"""
  
        self.scenes = {
            "start": Scene(
                "start",
                "You wake up in a dark forest. The trees loom ominously around you.",
                {
                    "Go north toward the mountains": "mountain_path",
                    "Go east toward the river": "river",
                    "Go west into the dark woods": "dark_woods"
                },
                item="health_potion"
            ),
            "mountain_path": Scene(
                "mountain_path",
                "The path winds steeply upward. The air grows thinner as you climb.",
                {
                    "Continue climbing": "mountain_top",
                    "Descend back to the forest": "start",
                    "Search the area": "mountain_search"
                },
                enemy={"name": "mountain troll", "health": 50, "damage": 15}
            ),
            "river": Scene(
                "river",
                "A swift river blocks your path. The water looks deep and dangerous.",
                {
                    "Attempt to swim across": "river_swim",
                    "Follow the river north": "river_north",
                    "Return to the forest": "start"
                },
                item="rusty_sword"
            ),
            "dark_woods": Scene(
                "dark_woods",
                "The trees grow denser, blocking most of the sunlight. Strange noises echo around you.",
                {
                    "Search for the source of the noises": "witch_hut",
                    "Quickly leave this area": "start",
                    "Hide and observe": "dark_woods_hide"
                },
                enemy={"name": "giant spider", "health": 30, "damage": 10}
            ),
            "mountain_top": Scene(
                "mountain_top",
                "You reach the summit. A magnificent view stretches before you, but something glitters in the snow.",
                {
                    "Investigate the glittering object": "treasure",
                    "Rest and enjoy the view": "start",
                    "Descend the mountain": "mountain_path"
                },
                item="golden_amulet"
            ),
            "treasure": Scene(
                "treasure",
                "You uncover a chest full of gold and jewels! This would make you rich beyond your wildest dreams.",
                {
                    "Take the treasure": "victory",
                    "Leave it untouched": "mountain_top"
                }
            ),
            "victory": Scene(
                "victory",
                "Congratulations! You've completed your adventure successfully!",
                {"Play again": "start", "Quit game": "quit"}
            ),
            "game_over": Scene(
                "game_over",
                "Your adventure has come to an end.",
                {"Try again": "start", "Quit game": "quit"}
            )
        }
    
    def generate_loot(self) -> Generator[str, None, None]:
        """Generator: Yield random loot drops"""
        loot = [
            "health_potion", "magic_ring", "iron_helmet", 
            "enchanted_sword", "gold_coins", "ancient_scroll"
        ]
        while True:
            yield random.choice(loot)
    
    def start_new_game(self) -> None:
        """Initialize a new game"""
        name = input("Enter your character's name: ")
        self.player = Player(name)
        print(f"\nWelcome, {name}! Your adventure begins...")
        self.play_scene(self.scenes["start"])
    
    def play_scene(self, scene: Scene) -> None:
        """Handle the current scene and player choices"""
        if not self.player:
            return
        
        self.player.current_scene = scene.scene_id
        scene.display()

        if scene.enemy:
            self.handle_enemy_encounter(scene)
            if self.player.health <= 0:
                self.game_over()
                return

        if scene.item and not scene.item.startswith("_"):
            self.handle_item_pickup(scene)
        
        # Get player choice
        while True:
            try:
                choice = self.get_player_choice(scene)
                self.handle_choice(choice, scene)
                break
            except ValueError as e:
                print(f"\nInvalid choice: {e}")
    
    def handle_enemy_encounter(self, scene: Scene) -> None:
        """Handle combat with an enemy"""
        if not scene.enemy or not self.player:
            return
        
        enemy = scene.enemy
        print(f"\nThe {enemy['name']} attacks you!")
        
        while enemy['health'] > 0 and self.player.health > 0:
            action = input("\nChoose action: [1] Attack, [2] Use item, [3] Flee: ")
            
            if action == "1":  # Attack
                damage = random.randint(5, 15)
                enemy['health'] = max(0, enemy['health'] - damage)
                print(f"\nYou hit the {enemy['name']} for {damage} damage!")
                
                if enemy['health'] <= 0:
                    print(f"\nYou defeated the {enemy['name']}!")
                    loot = next(self.generate_loot())
                    self.player.add_to_inventory(loot)
                    break
                
                # Enemy counterattack
                self.player.take_damage(enemy['damage'])
            
            elif action == "2":  # Use item
                if not self.player.inventory:
                    print("\nYour inventory is empty!")
                    continue
                
                print("\nYour items:")
                for i, item in enumerate(self.player.inventory, 1):
                    print(f"{i}. {item}")
                
                try:
                    item_choice = int(input("Select item to use (0 to cancel): ")) - 1
                    if item_choice == -1:
                        continue
                    item = self.player.inventory[item_choice]
                    
                    if item == "health_potion":
                        self.player.heal(30)
                        self.player.inventory.pop(item_choice)
                    else:
                        print(f"\nYou can't use {item} in combat!")
                
                except (ValueError, IndexError):
                    print("\nInvalid item selection")
            
            elif action == "3":  # Flee
                if random.random() < 0.5:  # 50% chance to flee
                    print("\nYou successfully fled from battle!")
                    self.player.current_scene = "start"
                    self.play_scene(self.scenes["start"])
                    return
                else:
                    print("\nYou failed to flee!")
                    self.player.take_damage(enemy['damage'])
            
            else:
                print("\nInvalid action!")
    
    def handle_item_pickup(self, scene: Scene) -> None:
        """Handle item pickup from the scene"""
        if not scene.item or not self.player:
            return
        
        pickup = input(f"\nWould you like to take the {scene.item}? (y/n): ").lower()
        if pickup == 'y':
            self.player.add_to_inventory(scene.item)
            scene.item = f"_taken_{scene.item}"  
    
    def get_player_choice(self, scene: Scene) -> str:
        """Get and validate player choice"""
        if not scene.choices:
            return "quit"
        
        max_choice = len(scene.choices)
        if scene.enemy:
            max_choice += 2  
        
        while True:
            try:
                choice = input("\nEnter your choice: ")
                if not choice.isdigit():
                    raise ValueError("Please enter a number")
                
                choice_num = int(choice)
                if choice_num < 1 or choice_num > max_choice:
                    raise ValueError(f"Please enter a number between 1 and {max_choice}")
                
                return choice
            except ValueError as e:
                print(f"Invalid input: {e}")
    
    def handle_choice(self, choice: str, scene: Scene) -> None:
        """Process the player's choice"""
        choice_num = int(choice)
        choices_list = list(scene.choices.items())
        
        # Handle enemy scene choices (attack or flee)
        if scene.enemy and choice_num > len(choices_list):
            if choice_num == len(choices_list) + 1:  # Attack
                return  # Already handled in combat
            elif choice_num == len(choices_list) + 2:  # Flee
                self.player.current_scene = "start"
                self.play_scene(self.scenes["start"])
                return
        
        # Normal scene transition
        selected_choice = choices_list[choice_num - 1]
        next_scene_id = selected_choice[1]
        
        if next_scene_id == "quit":
            print("\nThanks for playing!")
            exit()
        
        self.play_scene(self.scenes[next_scene_id])
    
    def game_over(self) -> None:
        """Handle game over scenario"""
        print("\n=== GAME OVER ===")
        self.play_scene(self.scenes["game_over"])
    
    @save_progress
    def play_scene(self, scene: Scene) -> None:
        """Decorated version that gets wrapped by save_progress"""
        # The actual implementation is above
        pass
    
    def save_game(self) -> None:
        """Save the current game state"""
        if not self.player:
            return
        
        save_data = {
            "player": {
                "name": self.player.name,
                "health": self.player.health,
                "max_health": self.player.max_health,
                "inventory": self.player.inventory,
                "current_scene": self.player.current_scene
            }
        }
        
        with open(self.game_file, "w") as f:
            json.dump(save_data, f)
    
    def load_game(self) -> bool:
        """Load a saved game"""
        try:
            with open(self.game_file, "r") as f:
                save_data = json.load(f)
            
            self.player = Player(
                name=save_data["player"]["name"],
                health=save_data["player"]["health"]
            )
            self.player.max_health = save_data["player"]["max_health"]
            self.player.inventory = save_data["player"]["inventory"]
            self.player.current_scene = save_data["player"]["current_scene"]
            
            print(f"\nWelcome back, {self.player.name}!")
            self.play_scene(self.scenes[self.player.current_scene])
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return False

def save_progress(func):
    """Decorator to save game progress after each move"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.save_game()
        return result
    return wrapper

def main():
    game = Game()
    
    print("=== TEXT ADVENTURE RPG ===")
    print("1. New Game")
    print("2. Load Game")
    
    while True:
        choice = input("\nSelect option: ")
        if choice == "1":
            game.start_new_game()
            break
        elif choice == "2":
            if game.load_game():
                break
            else:
                print("No saved game found. Starting new game.")
                game.start_new_game()
                break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()