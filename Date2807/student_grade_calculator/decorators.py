import json
import functools

CACHE_FILE = "gpa_cache.json"

def memoize(func):
    @functools.wraps(func)
    def wrapper(student):
        try:
            with open(CACHE_FILE, "r") as f:
                cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            cache = {}

        if student.student_id in cache:
            return cache[student.student_id]

        result = func(student)
        cache[student.student_id] = result

        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)

        return result
    return wrapper
