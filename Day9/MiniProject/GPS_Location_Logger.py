locations = [
    (12.9716, 77.5946),  
    (28.6139, 77.2090),   
    (19.0760, 72.8777),   
    (13.0827, 80.2707),  
    (17.3850, 78.4867)    
]


recent = locations[-5:]
print("Recent locations:")
for lat, lon in recent: 
    print(f"Lat: {lat}, Lon: {lon}")

try:
    locations[0] = (12.3456, 77.8910)
except TypeError:
    print("\nCannot modify tuple - immutability enforced")