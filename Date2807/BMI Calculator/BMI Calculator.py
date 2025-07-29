import json
from functools import wraps
from typing import List, Dict, Generator

class Person:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.validate_inputs()
    
    def validate_inputs(self) -> None:
        """Exception handling for negative weight/height"""
        if self.weight_kg <= 0:
            raise ValueError("Weight must be positive")
        if self.height_m <= 0:
            raise ValueError("Height must be positive")
    
    def calculate_bmi(self) -> float:
        """Compute BMI (weight / height^2)"""
        return self.weight_kg / (self.height_m ** 2)
    
    def classify_bmi(self) -> str:
        """Classify BMI into health categories"""
        bmi = self.calculate_bmi()
        
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def health_risk(self) -> str:
        """Determine health risk based on BMI classification"""
        category = self.classify_bmi()
        
        if category == "Underweight":
            return "Possible nutritional deficiency and osteoporosis"
        elif category == "Normal weight":
            return "Low risk (healthy range)"
        elif category == "Overweight":
            return "Moderate risk of developing heart disease, high blood pressure, stroke, diabetes"
        else:
            return "High risk of developing heart disease, high blood pressure, stroke, diabetes"
    
    def to_dict(self) -> Dict:
        """Convert person data to dictionary for JSON storage"""
        return {
            "name": self.name,
            "weight_kg": self.weight_kg,
            "height_m": self.height_m,
            "bmi": round(self.calculate_bmi(), 1),
            "category": self.classify_bmi(),
            "risk": self.health_risk()
        }

class BMICalculator:
    def __init__(self, history_file: str = "bmi_history.json"):
        self.history_file = history_file
        self.people: List[Person] = []
        self.load_history()
    
    def load_history(self) -> None:
        """File handling: Load BMI history from JSON"""
        try:
            with open(self.history_file, 'r') as f:
                data = json.load(f)
                for entry in data:
                    try:
                        person = Person(
                            entry["name"],
                            entry["weight_kg"],
                            entry["height_m"]
                        )
                        self.people.append(person)
                    except (KeyError, ValueError):
                        continue
        except (FileNotFoundError, json.JSONDecodeError):
            pass  
    
    def save_history(self) -> None:
        """Save current BMI history to JSON file"""
        data = [person.to_dict() for person in self.people]
        with open(self.history_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_person(self, name: str, weight_kg: float, height_m: float) -> None:
        """Add a new person to the calculator"""
        try:
            person = Person(name, weight_kg, height_m)
            self.people.append(person)
            self.save_history()
            print(f"\nAdded {name} to BMI records")
        except ValueError as e:
            print(f"\nError: {e}")
    
    def find_obese_people(self) -> Generator[Person, None, None]:
        """Generator: Yield people in 'Obese' category"""
        for person in self.people:
            if person.classify_bmi() == "Obese":
                yield person
    
    def display_results(self, person: Person) -> None:
        """Display BMI results for a person"""
        print("\n=== BMI Results ===")
        print(f"Name: {person.name}")
        print(f"Weight: {person.weight_kg} kg")
        print(f"Height: {person.height_m} m")
        print(f"BMI: {person.calculate_bmi():.1f}")
        print(f"Category: {person.classify_bmi()}")
        print(f"Health Risk: {person.health_risk()}")
        print("==================")

def unit_converter(func):
    """Decorator: Convert between kg/lb and cm/ft"""
    @wraps(func)
    def wrapper(*args, **kwargs):
      
        weight_unit = kwargs.get('weight_unit', input("Weight unit (kg/lb): ").lower())
        height_unit = kwargs.get('height_unit', input("Height unit (m/cm/ft): ").lower())
        
        weight = kwargs.get('weight', float(input("Enter weight: ")))
        height = kwargs.get('height', float(input("Enter height: ")))
        
        if weight_unit == "lb":
            weight = weight * 0.453592  
        
        if height_unit == "cm":
            height = height / 100  
        elif height_unit == "ft":
            height = height * 0.3048  
        
        return func(*args, weight_kg=weight, height_m=height, **kwargs)
    return wrapper

@unit_converter
def add_person_interactive(calculator: BMICalculator, name: str, weight_kg: float, height_m: float):
    """Interactive function to add a person with unit conversion"""
    calculator.add_person(name, weight_kg, height_m)

def main():
    calculator = BMICalculator()
    
    print("BMI Calculator")
    print("==============")
    
    while True:
        print("\nMenu:")
        print("1. Calculate BMI for new person")
        print("2. View all records")
        print("3. View obese individuals")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            name = input("Enter name: ")
            try:
                add_person_interactive(calculator, name, weight_kg=0, height_m=0)

                if calculator.people:
                    calculator.display_results(calculator.people[-1])
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            if not calculator.people:
                print("\nNo records found")
                continue
            
            print("\nAll BMI Records:")
            for person in calculator.people:
                calculator.display_results(person)
        
        elif choice == "3":
            obese_people = list(calculator.find_obese_people())
            if not obese_people:
                print("\nNo obese individuals in records")
                continue
            
            print("\nObese Individuals (High Risk):")
            for person in obese_people:
                calculator.display_results(person)
        
        elif choice == "4":
            calculator.save_history()
            print("\nGoodbye! Your BMI history has been saved.")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()