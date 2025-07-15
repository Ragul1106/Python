weather = {}

def add_temp(city, temp):
    weather.setdefault(city, []).append(temp)

def hottest_city():
    return max(weather.items(), 
               key=lambda x: sum(x[1])/len(x[1]))[0]

add_temp("Chennai", 35)
print("Hottest:", hottest_city())