monday = {'#news', '#sports'}
tuesday = {'#tech', '#news'}
weekly = set()

weekly.update(monday)
weekly.update(tuesday)
print("Weekly trends:", weekly)
print("Unique to Monday:", monday - tuesday)