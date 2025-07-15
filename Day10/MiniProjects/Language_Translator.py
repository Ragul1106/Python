translator = {"hello": "வணக்கம்", "good": "நல்ல"}

def add_translation(eng, tam):
    translator[eng] = tam

def reverse_dict():
    return {v: k for k, v in translator.items()}

print("Tamil for 'hello':", translator.get("hello", "Not found"))
print("Reversed:", reverse_dict())